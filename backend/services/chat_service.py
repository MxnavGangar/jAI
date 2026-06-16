from providers.vectorstore.factory import (
    get_vectorstore_provider
)

from providers.language_models.factory import (
    get_llm_provider
)

from utils.prompt_loader import (
    load_prompt
)


class ChatService:

    def __init__(self):

        self.vectorstore = (
            get_vectorstore_provider()
        )

        self.llm = (
            get_llm_provider()
        )

    def chat(
        self,
        query: str
    ):

        retrieval_result = (
            self.vectorstore.search(
                query=query,
                top_k=3
            )
        )

        chunks = (
            retrieval_result["documents"]
        )

        metadatas = (
            retrieval_result["metadatas"]
        )

        context = "\n\n".join(
            chunks
        )

        template = (
            load_prompt(
                "rag_prompt.txt"
            )
        )

        prompt = (
            template.format(
                context=context,
                question=query
            )
        )

        answer = (
            self.llm.generate(
                system_prompt="You are JAI.",
                user_prompt=prompt
            )
        )

        sources = []

        for metadata in metadatas:

            if (
                metadata and
                "source" in metadata
            ):

                sources.append(
                    metadata["source"]
                )

        return {
            "answer": answer,
            "sources": list(
                set(sources)
            )
        }