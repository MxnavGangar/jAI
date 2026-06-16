from rag.ingestion.loaders.text_loader import (
    TextLoader
)

from rag.ingestion.chunker import (
    TextChunker
)


class DocumentProcessor:

    def process(
        self,
        filepath: str
    ):

        loader = TextLoader()

        text = loader.load(
            filepath
        )

        chunker = TextChunker()

        return chunker.chunk(
            text
        )