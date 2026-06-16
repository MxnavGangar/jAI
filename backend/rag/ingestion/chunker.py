class TextChunker:

    def chunk(self, text: str):

        chunks = [
            chunk.strip()
            for chunk in text.split("---")
            if chunk.strip()
        ]

        return chunks