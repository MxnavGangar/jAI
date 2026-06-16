from core.settings import settings

from providers.vectorstore.chroma import (
    ChromaProvider
)


def get_vectorstore_provider():

    if (
        settings.vectorstore_provider
        == "chroma"
    ):
        return ChromaProvider()

    raise ValueError(
        "Unsupported vector store"
    )