from fastapi import APIRouter

from core.settings import settings

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "llm_provider": settings.llm_provider,
        "embedding_provider": settings.embedding_provider,
        "vectorstore_provider": settings.vectorstore_provider
    }