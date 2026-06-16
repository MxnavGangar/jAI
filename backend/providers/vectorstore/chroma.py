import uuid
import chromadb

from providers.embeddings.factory import (
    get_embedding_provider
)

from providers.vectorstore.base import (
    VectorStoreProvider
)


class ChromaProvider(VectorStoreProvider):

    def __init__(self):

        self.embedding_provider = (
            get_embedding_provider()
        )

        self.client = (
            chromadb.PersistentClient(
                path="./vectordb"
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="jai_documents"
            )
        )

    def add_documents(
        self,
        documents
    ):

        for doc in documents:

            embedding = (
                self.embedding_provider.embed(
                    doc
                )
            )

            self.collection.add(
                ids=[
                    str(uuid.uuid4())
                ],
                documents=[
                    doc
                ],
                embeddings=[
                    embedding
                ],
                metadatas=[
                    {
                        "source": "jio_help_center.txt"
                    }
                ]
            )

    def search(
        self,
        query,
        top_k=3
    ):

        embedding = (
            self.embedding_provider.embed(
                query
            )
        )

        results = (
            self.collection.query(
                query_embeddings=[
                    embedding
                ],
                n_results=top_k
            )
        )

        return {
            "documents": (
                results["documents"][0]
                if results["documents"]
                else []
            ),
            "metadatas": (
                results["metadatas"][0]
                if results["metadatas"]
                else []
            )
        }

    def clear(self):

        self.client.delete_collection(
            "jai_documents"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="jai_documents"
            )
        )