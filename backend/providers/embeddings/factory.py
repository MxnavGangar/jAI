from core.settings import settings

from providers.embeddings.bge import BGEProvider


def get_embedding_provider():

    provider = settings.embedding_provider

    if provider == "bge":
        return BGEProvider()

    raise ValueError(
        f"Unsupported embedding provider: {provider}"
    )