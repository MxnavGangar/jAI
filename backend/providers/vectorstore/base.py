from abc import ABC, abstractmethod


class VectorStoreProvider(ABC):

    @abstractmethod
    def add_documents(
        self,
        documents
    ):
        pass

    @abstractmethod
    def search(
        self,
        query,
        top_k=3
    ):
        pass