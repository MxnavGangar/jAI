from rag.ingestion.processor import (
    DocumentProcessor
)

from providers.vectorstore.factory import (
    get_vectorstore_provider
)


class IngestionService:

    def ingest(
        self,
        filepath: str
    ):

        processor = (
            DocumentProcessor()
        )

        chunks = processor.process(
            filepath
        )

        vectorstore = (
            get_vectorstore_provider()
        )

        vectorstore.add_documents(
            chunks
        )

        return len(chunks)