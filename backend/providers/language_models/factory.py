from core.settings import settings

from providers.language_models.groq import (
    GroqProvider
)


def get_llm_provider():

    if settings.llm_provider == "groq":
        return GroqProvider()

    raise ValueError(
        f"Unsupported LLM provider: "
        f"{settings.llm_provider}"
    )