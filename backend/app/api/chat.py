from fastapi import APIRouter
from app.services.rag_service import search_pdf

router = APIRouter()


@router.post("/ask")
async def ask_question(data: dict):

    question = data.get("question", "")

    answer = search_pdf(question)

    return {
        "question": question,
        "answer": answer
    }