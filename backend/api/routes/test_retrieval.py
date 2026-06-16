from fastapi import APIRouter

from providers.vectorstore.factory import (
    get_vectorstore_provider
)

router = APIRouter()


@router.get("/test-retrieval")
def test_retrieval():

    vectorstore = (
        get_vectorstore_provider()
    )

    result = (
        vectorstore.search(
            "How can I activate my esim?"
        )
    )

    return result