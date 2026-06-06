from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# Models
from app.models.user import User
from app.models.chat_history import ChatHistory

# Routers
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.auth import router as auth_router
from app.api.history import router as history_router
from app.api.documents import router as documents_router
from app.api.delete_document import router as delete_router

app = FastAPI(
    title="NexusAI API",
    version="1.0.0"
)

# Create Tables
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(history_router)
app.include_router(documents_router)
app.include_router(delete_router)


@app.get("/")
def root():
    return {
        "message": "NexusAI Backend Running"
    }


@app.get("/dashboard/stats")
def dashboard_stats():
    return {
        "documents": 1,
        "questions": 128,
        "sources": 1,
        "users": 1
    }