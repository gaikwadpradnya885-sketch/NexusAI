from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/dashboard/stats")
def get_stats():

    documents = 0

    if os.path.exists("uploads"):
        documents = len([
            f for f in os.listdir("uploads")
            if f.endswith(".pdf")
        ])

    return {
        "documents": documents,
        "questions": 128,
        "sources": documents,
        "users": 1
    }