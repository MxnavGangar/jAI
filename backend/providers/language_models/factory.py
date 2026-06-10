from core.settings import settings

from providers.language_models.grok import GrokProvider
from providers.language_models.gemini import GeminiProvider
from providers.language_models.ollama import OllamaProvider


def get_llm_provider():

    provider = settings.llm_provider.lower()

    if provider == "grok":
        return GrokProvider()

    elif provider == "gemini":
        return GeminiProvider()

    elif provider == "ollama":
        return OllamaProvider()

    raise ValueError(
        f"Unsupported provider: {provider}"
    )