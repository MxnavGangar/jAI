from sentence_transformers import SentenceTransformer

from providers.embeddings.base import EmbeddingProvider


class BGEProvider(EmbeddingProvider):

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed(self, text: str):
        return self.model.encode(text).tolist()