from fastapi import APIRouter

from services.ingestion_service import (
    IngestionService
)

router = APIRouter()


@router.get("/ingest")
def ingest():

    service = (
        IngestionService()
    )

    count = service.ingest(
        "data/raw/jio_faq.txt"
    )

    return {
        "chunks_ingested": count
    }