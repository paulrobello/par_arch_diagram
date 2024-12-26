"""Main entry point for par_arch_diagram."""

import json
import os
import subprocess
import time
from pathlib import Path
from textwrap import dedent
from typing import Annotated

import typer
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from par_ai_core.llm_config import LlmConfig, llm_run_manager
from par_ai_core.llm_providers import (
    LlmProvider,
    provider_default_models,
    provider_env_key_names,
)
from par_ai_core.pricing_lookup import PricingDisplay, mk_usage_metadata, show_llm_cost
from par_ai_core.provider_cb_info import get_parai_callback
from rich.panel import Panel
from rich.text import Text

from . import __application_binary__, __application_title__, __version__
from .utils import console

load_dotenv()
load_dotenv(Path(f"~/.{__application_binary__}.env").expanduser())

# Initialize Typer app
app = typer.Typer(help="CLI to to generate architecture diagrams.")


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        print(f"{__application_title__}: {__version__}")
        raise typer.Exit()


# pylint: disable=too-many-statements,dangerous-default-value,too-many-arguments, too-many-locals, too-many-positional-arguments, too-many-branches
@app.command()
def main(
    iac_folder: Annotated[Path, typer.Option("--iac", "-i", help="IAC file or folder to process")] = Path(
        f"{Path(__file__).parent}/readme-iac.md"
    ),
    ai_provider: Annotated[
        LlmProvider,
        typer.Option("--ai-provider", "-a", help="AI provider to use for processing"),
    ] = LlmProvider.ANTHROPIC,
    model: Annotated[
        str | None,
        typer.Option(
            "--model",
            "-m",
            help="AI model to use for processing. If not specified, a default model will be used.",
        ),
    ] = None,
    ai_base_url: Annotated[
        str | None,
        typer.Option(
            "--ai-base-url",
            "-b",
            help="Override the base URL for the AI provider.",
        ),
    ] = None,
    temperature: Annotated[
        float,
        typer.Option(
            "--temperature",
            "-t",
            help="Temperature to use for processing. If not specified, a default temperature will be used.",
        ),
    ] = 0.5,
    prompt_cache: Annotated[
        bool,
        typer.Option("--prompt-cache", "-c", help="Enable prompt cache for Anthropic provider"),
    ] = False,
    output_folder: Annotated[
        Path,
        typer.Option("--output-folder", "-o", help="Specify the location of the output folder"),
    ] = Path("./output"),
    system_prompt: Annotated[
        Path | None,
        typer.Option("--system-prompt", "-s", help="Path to the system prompt file"),
    ] = None,
    diagram_name: Annotated[
        str | None,
        typer.Option(
            "--diagram-name",
            "-n",
            help="Name of the diagram to generate. If not specified, a default name will be used.",
        ),
    ] = None,
    pricing: Annotated[
        PricingDisplay,
        typer.Option("--pricing", "-p", help="Enable pricing summary display"),
    ] = PricingDisplay.PRICE,
    version: Annotated[  # pylint: disable=unused-argument
        bool | None,
        typer.Option("--version", "-v", callback=version_callback, is_eager=True),
    ] = None,
):
    """Generate architecture diagrams."""

    if not iac_folder.exists():
        console.print(f"[bold red]IAC folder: {iac_folder} does not exist. Exiting...[/bold red]")
        raise typer.Exit(1)

    if not system_prompt:
        system_prompt = Path(__file__).parent / "system_prompt.md"
    if not system_prompt.exists():
        console.print(f"[bold red]System prompt file not found: {system_prompt}[/bold red]")
        raise typer.Exit(1)

    if not model:
        model = provider_default_models[ai_provider]
    if not model:
        console.print("[bold red]Model not specified and no default available. Exiting...[/bold red]")
        raise typer.Exit(1)

    if ai_provider not in [LlmProvider.OLLAMA, LlmProvider.BEDROCK]:
        key_name = provider_env_key_names[ai_provider]
        if not os.environ.get(key_name):
            console.print(f"[bold red]{key_name} environment variable not set. Exiting...[/bold red]")
            raise typer.Exit(1)

    llm_config = LlmConfig(
        provider=ai_provider,
        model_name=model,
        temperature=temperature,
        base_url=ai_base_url,
    )

    chat_model = llm_config.build_chat_model()

    if prompt_cache and not isinstance(chat_model, ChatAnthropic):
        console.print("[bold yellow]Prompt cache is only supported for ANTHROPIC provider.")
        prompt_cache = False
    if not diagram_name:
        diagram_name = "Arch Diagram"

    console.print(
        Panel.fit(
            Text.assemble(
                ("AI Provider: ", "cyan"),
                (f"{str(ai_provider.value)}", "green"),
                "\n",
                ("Model: ", "cyan"),
                (f"{model}", "green"),
                "\n",
                ("AI Provider Base URL: ", "cyan"),
                (f"{ai_base_url or 'default'}", "green"),
                "\n",
                ("Prompt Cache: ", "cyan"),
                (f"{prompt_cache}", "green"),
                "\n",
                ("Temperature: ", "cyan"),
                (f"{temperature}", "green"),
                "\n",
                ("System Prompt: ", "cyan"),
                (f"{system_prompt}", "green"),
                "\n",
                ("IAC Folder: ", "cyan"),
                (f"{iac_folder}", "green"),
                "\n",
                ("Output Folder: ", "cyan"),
                (f"{output_folder}", "green"),
                "\n",
                ("Diagram Name: ", "cyan"),
                (f"{diagram_name or 'default'}", "green"),
            ),
            title="[bold]App Configuration",
            border_style="bold",
        )
    )

    start_time = time.time()
    try:
        system_message = system_prompt.read_text(encoding="utf-8")

        if not output_folder.exists():
            output_folder.mkdir(parents=True, exist_ok=True)
        output_file = output_folder / f"{diagram_name.replace(' ', '_')}.py"

        if output_file.exists():
            console.print(f"[bold yellow]Removing existing output file: {output_file}")
            output_file.unlink()
        usage_metadata = mk_usage_metadata()
        with console.status("[bold green]Processing IAC data...") as status:
            with get_parai_callback() as cb:
                if iac_folder.is_file():
                    iac_info = f"<file>\n<file_name>{iac_folder.name}</file_name>\n<file_content>\n{iac_folder.read_text(encoding='utf-8').strip()}\n</file>"  # noqa: E501
                elif iac_folder.is_dir():
                    iac_info = "\n".join(
                        [
                            f"<file>\n<file_name>{entry.name}</file_name>\n<file_content>\n{entry.read_text(encoding='utf-8').strip()}\n</file_content>\n</file>"
                            for entry in iac_folder.iterdir()
                            if entry.is_file()
                        ]
                    )
                else:
                    raise ValueError(f"IAC folder: {iac_folder} is not a file or directory.")

                status.update("[bold cyan]Generating diagram code...")
                history = [
                    (
                        "system",
                        system_message,
                    ),
                    (
                        "user",
                        [
                            {
                                "type": "text",
                                "text": dedent(
                                    f"""
                                <diagram_file_name>{output_file.absolute().as_posix().split(".")[0:-1]}</diagram_file_name>
                                <iac_info>
                                {iac_info}
                                </iac_info>
                                """
                                ),
                            }
                        ],
                    ),
                ]

                if prompt_cache:
                    if isinstance(chat_model, ChatAnthropic):
                        history[1][1][0]["cache_control"] = {"type": "ephemeral"}  # type: ignore

                (output_folder / "history.json").write_text(
                    json.dumps(history, indent=2, default=str), encoding="utf-8"
                )

                max_iterations = 10
                iterations = 0
                valid = False
                while not valid and iterations < max_iterations:
                    iterations += 1
                    response = chat_model.invoke(history, config=llm_run_manager.get_runnable_config(chat_model.name))
                    usage_metadata = cb.usage_metadata
                    # console.print(Pretty(response))

                    console.print(f"[bold cyan]Saving diagram code to {output_file}...")
                    output_file.write_text(str(response.content), encoding="utf-8")
                    history.append(("assistant", str(response.content)))
                    (output_folder / "history.json").write_text(
                        json.dumps(history, indent=2, default=str), encoding="utf-8"
                    )

                    status.update("[bold cyan]Generating diagram image...")
                    try:
                        proc = subprocess.run(
                            ["uv", "run", "python", output_file.absolute()],
                            cwd=Path(__file__).parent,
                            capture_output=True,
                            check=False,
                        )
                        output = proc.stdout.decode("utf-8")
                        stderr = proc.stderr.decode("utf-8")
                        if proc.returncode != 0:
                            raise Exception(f"Error executing diagram code: {stderr or output}")
                        valid = True
                    except Exception as e:  # pylint: disable=broad-except
                        console.print(f"[bold red]Error executing diagram code: {str(e).splitlines()[-1]}[/bold red]")
                        history.append(
                            (
                                "user",
                                f"Error executing diagram code: {str(e)}",
                            )
                        )

            if not valid:
                console.print("[bold red]Error generating diagram code. Please try again.[/bold red]")
                raise typer.Exit(1)

        duration = time.time() - start_time
        console.print(Panel.fit(f"Done in {duration:.2f} seconds."))

    except Exception as e:  # pylint: disable=broad-except
        console.print(e)
        console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")

    show_llm_cost(usage_metadata, console=console, show_pricing=pricing)


if __name__ == "__main__":
    app()
