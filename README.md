# PAR Arch Diagram

![Runs on Linux | MacOS | Windows](https://img.shields.io/badge/runs%20on-Linux%20%7C%20MacOS%20%7C%20Windows-blue)
![Arch x86-63 | ARM | AppleSilicon](https://img.shields.io/badge/arch-x86--64%20%7C%20ARM%20%7C%20AppleSilicon-blue)  
![PyPI - License](https://img.shields.io/pypi/l/par_arch_diagram)

PAR Arch Diagram is a cli tool that leverages AI to generate architecture diagrams.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/probello3)

## Features

- AI-powered iac analysis and diagramming
- [PAR AI Core](https://github.com/paulrobello/par_ai_core).

## Prerequisites

To install PAR Arch Diagram, make sure you have Python 3.11.

### [uv](https://pypi.org/project/uv/) is recommended

#### Linux and Mac
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installation


### Source

Then, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/paulrobello/par_arch_diagram.git
cd par_arch_diagram
uv tool install .
```
### GitHub

```shell
uv tool install git+https://github.com/paulrobello/par_arch_diagram
```

## Update

### Source

```shell
cd par_arch_diagram
git pull
uv tool install . -U --force
```

### GitHub

```shell
uv tool install -U --force git+https://github.com/paulrobello/par_arch_diagram
```

## Usage

To use PAR Arch Diagram, you can run it from the command line with various options. Here's a basic example:
Ensure you have the AI provider api key in your environment.
You can also store your key in the file `~/.par_arch_diagram.env` as follows:
```bash
GROQ_API_KEY= # is required for Groq. Get a free key from https://console_out.groq.com/
ANTHROPIC_API_KEY= # is required for Anthropic. Get a key from https://console_out.anthropic.com/
OPENAI_API_KEY= # is required for OpenAI. Get a key from https://platform.openai.com/account/api-keys
GITHUB_TOKEN= # is required for GitHub Models. Get a free key from https://github.com/marketplace/models
GOOGLE_API_KEY= # is required for Google Models. Get a free key from https://console_out.cloud.google.com
LANGCHAIN_API_KEY= # is required for Langchain Langsmith tracing. Get a free key from https://smith.langchain.com/settings
AWS_PROFILE= # is used for Bedrock authentication. The environment must already be authenticated with AWS.
#No key required to use with Ollama models.
```

### Running from source
```bash
uv run par_arch_diagram --iac ./my_iac_folder --ai-provider OPENAI --model gpt-4o -n MyDiagram
```

### Running if installed as tool
```bash
par_arch_diagram --iac ./my_iac_folder --ai-provider OPENAI --model gpt-4o
```

### Options

- `--iac`, `-i`: Path to the IAC folder (default: "../../readme-iac.md")
- `--ai-provider`, `-a`: AI provider to use for processing (default: "OPENAI")
- `--model`, `-m`: AI model to use for processing. If not specified, a default model will be used based on the provider.
- `--ai-base-url`, `-b`: Override the base URL for the AI provider.
- `--output-folder`, `-o`: Specify the location of the output folder (default: "../../output")
- `--version`, `-v`: Show the version and exit
- `--cleanup`, `-c`: How to handle cleanup of output folder (choices: none, before, after, both) (default: none)
- `--system-prompt`, `-s`: Path to the system prompt file

### Examples

1. Basic usage with default options:
```bash
par_arch_diagram
```

2. Specifying a custom IAC folder and AI provider:
```bash
par_arch_diagram --iac ./my_iac_folder --ai-provider ANTHROPIC
```

3. Using a specific model and custom output folder:
```bash
par_arch_diagram --model gpt-4 --output-folder ./custom_output
```

4. Overriding the AI provider base URL:
```bash
par_arch_diagram --ai-provider OPENAI --ai-base-url https://custom-openai-endpoint.com
```

5. Using a custom system prompt:
```bash
par_arch_diagram --system-prompt ./my_system_prompt.md
```

## Whats New
- Version 0.1.2:
  - Updated to use PAR AI Core
- Version 0.1.1:
  - Updated AI Lib and dependencies
- Version 0.1.0:
  - Initial release

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Paul Robello - probello@gmail.com
