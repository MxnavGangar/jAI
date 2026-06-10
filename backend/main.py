from fastapi import FastAPI

from api.routes.health import router as health_router

app = FastAPI(
    title="JAI Core",
    version="1.0.0"
)

app.include_router(health_router)

from api.routes.test_embedding import (
    router as embedding_router
)

app.include_router(embedding_router)