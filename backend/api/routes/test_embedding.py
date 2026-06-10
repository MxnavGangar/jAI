from fastapi import APIRouter

from providers.embeddings.factory import (
    get_embedding_provider
)

router = APIRouter()


@router.get("/test-embedding")
def test_embedding():

    provider = get_embedding_provider()

    vector = provider.embed(
        "Hello JAI"
    )

    return {
        "dimension": len(vector)
    }