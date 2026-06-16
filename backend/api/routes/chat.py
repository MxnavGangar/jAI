from fastapi import APIRouter

from api.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from services.chat_service import (
    ChatService
)

router = APIRouter()

service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    result = (
        service.chat(
            request.query
        )
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )