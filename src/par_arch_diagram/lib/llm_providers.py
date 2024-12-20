"""LLM provider types."""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum


@dataclass
class LangChainConfig:
    """Langchain config."""

    tracing: bool = False
    project: str = "parllama"
    base_url: str = "https://api.smith.langchain.com"
    api_key: str = ""


class LlmProvider(str, Enum):
    """Llm provider types."""

    OLLAMA = "Ollama"
    OPENAI = "OpenAI"
    GROQ = "Groq"
    XAI = "XAI"
    ANTHROPIC = "Anthropic"
    GOOGLE = "Google"
    BEDROCK = "Bedrock"
    GITHUB = "Github"
    LLAMACPP = "LlamaCpp"


llm_provider_types: list[LlmProvider] = list(LlmProvider)
llm_provider_names: list[str] = [p.value.lower() for p in llm_provider_types]

provider_base_urls: dict[LlmProvider, str | None] = {
    LlmProvider.OLLAMA: "http://localhost:11434",
    LlmProvider.LLAMACPP: "http://localhost:8080/v1",
    LlmProvider.OPENAI: None,
    LlmProvider.GROQ: None,
    LlmProvider.XAI: None,
    LlmProvider.ANTHROPIC: None,
    LlmProvider.GOOGLE: None,
    LlmProvider.BEDROCK: None,
    LlmProvider.GITHUB: "https://models.inference.ai.azure.com",
}

provider_default_models: dict[LlmProvider, str] = {
    LlmProvider.OLLAMA: "",
    LlmProvider.LLAMACPP: "default",
    LlmProvider.OPENAI: "gpt-4o",
    LlmProvider.GROQ: "llama3-70b-8192",
    LlmProvider.XAI: "grok-beta",
    LlmProvider.ANTHROPIC: "claude-3-5-sonnet-20241022",
    LlmProvider.GOOGLE: "gemini-1.5-pro-002",
    LlmProvider.BEDROCK: "anthropic.claude-3-5-sonnet-20241022-v2:0",
    LlmProvider.GITHUB: "gpt-4o",
}

provider_light_models: dict[LlmProvider, str] = {
    LlmProvider.OLLAMA: "",
    LlmProvider.LLAMACPP: "default",
    LlmProvider.OPENAI: "gpt-4o-mini",
    LlmProvider.GROQ: "llama3-70b-8192",
    LlmProvider.XAI: "grok-beta",
    LlmProvider.ANTHROPIC: "claude-3-haiku-20240307",
    LlmProvider.GOOGLE: "gemini-2.0-flash-exp",
    LlmProvider.BEDROCK: "anthropic.claude-3-haiku-20240307-v1:0",
    LlmProvider.GITHUB: "gpt-4o-mini",
}

provider_vision_models: dict[LlmProvider, str] = {
    LlmProvider.OLLAMA: "",
    LlmProvider.LLAMACPP: "default",
    LlmProvider.OPENAI: "gpt-4o",
    LlmProvider.GROQ: "llama-3.2-90b-vision-preview",
    LlmProvider.XAI: "grok-vision-beta",
    LlmProvider.ANTHROPIC: "claude-3-5-sonnet-20241022",
    LlmProvider.GOOGLE: "gemini-1.5-pro-002",
    LlmProvider.BEDROCK: "anthropic.claude-3-5-sonnet-20241022-v2:0",
    LlmProvider.GITHUB: "gpt-4o",
}

provider_default_embed_models: dict[LlmProvider, str] = {
    LlmProvider.OLLAMA: "",  # nomic-embed-text:latest
    LlmProvider.LLAMACPP: "default",
    LlmProvider.OPENAI: "text-embedding-3-large",
    LlmProvider.GROQ: "",
    LlmProvider.XAI: "",
    LlmProvider.ANTHROPIC: "",
    LlmProvider.GOOGLE: "text-embedding-005",
    LlmProvider.BEDROCK: "amazon.titan-embed-text-v2:0",
    LlmProvider.GITHUB: "text-embedding-3-large",
}

provider_env_key_names: dict[LlmProvider, str] = {
    LlmProvider.OLLAMA: "",
    LlmProvider.LLAMACPP: "",
    LlmProvider.OPENAI: "OPENAI_API_KEY",
    LlmProvider.GROQ: "GROQ_API_KEY",
    LlmProvider.XAI: "XAI_API_KEY",
    LlmProvider.ANTHROPIC: "ANTHROPIC_API_KEY",
    LlmProvider.GOOGLE: "GOOGLE_API_KEY",
    LlmProvider.BEDROCK: "BEDROCK_API_KEY",
    LlmProvider.GITHUB: "GITHUB_TOKEN",
}


def get_provider_name_fuzzy(provider: str) -> str:
    """Get provider name fuzzy."""
    provider = provider.lower()
    for p in llm_provider_types:
        if p.value.lower() == provider:
            return p.value
        if p.value.lower().startswith(provider):
            return p.value
    return ""


@dataclass
class LlmProviderConfig:
    """Llm provider config."""

    default_model: str
    default_light_model: str
    default_vision_model: str
    default_embeddings_model: str
    supports_base_url: bool
    env_key_name: str


provider_config: dict[LlmProvider, LlmProviderConfig] = {
    LlmProvider.OLLAMA: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.OLLAMA],
        default_light_model=provider_light_models[LlmProvider.OLLAMA],
        default_vision_model=provider_vision_models[LlmProvider.OLLAMA],
        default_embeddings_model=provider_default_embed_models[LlmProvider.OLLAMA],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.OLLAMA],
    ),
    LlmProvider.OPENAI: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.OPENAI],
        default_light_model=provider_light_models[LlmProvider.OPENAI],
        default_vision_model=provider_vision_models[LlmProvider.OPENAI],
        default_embeddings_model=provider_default_embed_models[LlmProvider.OPENAI],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.OPENAI],
    ),
    LlmProvider.GROQ: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.GROQ],
        default_light_model=provider_light_models[LlmProvider.GROQ],
        default_vision_model=provider_vision_models[LlmProvider.GROQ],
        default_embeddings_model=provider_default_embed_models[LlmProvider.GROQ],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.GROQ],
    ),
    LlmProvider.XAI: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.XAI],
        default_light_model=provider_light_models[LlmProvider.XAI],
        default_vision_model=provider_vision_models[LlmProvider.XAI],
        default_embeddings_model=provider_default_embed_models[LlmProvider.XAI],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.XAI],
    ),
    LlmProvider.ANTHROPIC: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.ANTHROPIC],
        default_light_model=provider_light_models[LlmProvider.ANTHROPIC],
        default_vision_model=provider_vision_models[LlmProvider.ANTHROPIC],
        default_embeddings_model=provider_default_embed_models[LlmProvider.ANTHROPIC],
        supports_base_url=False,
        env_key_name=provider_env_key_names[LlmProvider.ANTHROPIC],
    ),
    LlmProvider.GOOGLE: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.GOOGLE],
        default_light_model=provider_light_models[LlmProvider.GOOGLE],
        default_vision_model=provider_vision_models[LlmProvider.GOOGLE],
        default_embeddings_model=provider_default_embed_models[LlmProvider.GOOGLE],
        supports_base_url=False,
        env_key_name=provider_env_key_names[LlmProvider.GOOGLE],
    ),
    LlmProvider.BEDROCK: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.BEDROCK],
        default_light_model=provider_light_models[LlmProvider.BEDROCK],
        default_vision_model=provider_vision_models[LlmProvider.BEDROCK],
        default_embeddings_model=provider_default_embed_models[LlmProvider.BEDROCK],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.BEDROCK],
    ),
    LlmProvider.GITHUB: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.GITHUB],
        default_light_model=provider_light_models[LlmProvider.GITHUB],
        default_vision_model=provider_vision_models[LlmProvider.GITHUB],
        default_embeddings_model=provider_default_embed_models[LlmProvider.GITHUB],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.GITHUB],
    ),
    LlmProvider.LLAMACPP: LlmProviderConfig(
        default_model=provider_default_models[LlmProvider.LLAMACPP],
        default_light_model=provider_light_models[LlmProvider.LLAMACPP],
        default_vision_model=provider_vision_models[LlmProvider.LLAMACPP],
        default_embeddings_model=provider_default_embed_models[LlmProvider.LLAMACPP],
        supports_base_url=True,
        env_key_name=provider_env_key_names[LlmProvider.LLAMACPP],
    ),
}


provider_env_key_names: dict[LlmProvider, str] = {k: v.env_key_name for k, v in provider_config.items()}


def provider_name_to_enum(name: str) -> LlmProvider:
    """Get LlmProvider enum from string."""
    return LlmProvider(name)


def is_provider_api_key_set(provider: LlmProvider) -> bool:
    """Check if API key is set for the provider."""
    if provider in [LlmProvider.OLLAMA, LlmProvider.LLAMACPP]:
        return True
    return len(os.environ.get(provider_env_key_names[provider], "")) > 0


def get_providers_with_api_keys() -> list[LlmProvider]:
    """Get providers with API keys."""
    return [p for p in LlmProvider if is_provider_api_key_set(p)]


def get_provider_select_options() -> list[tuple[str, LlmProvider]]:
    """Get provider select options."""
    return [
        (
            p,
            LlmProvider(p),
        )
        for p in get_providers_with_api_keys()
    ]
