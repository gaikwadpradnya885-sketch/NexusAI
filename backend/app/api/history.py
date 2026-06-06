from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.chat_history import ChatHistory

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/history")
def save_history(
    data: dict,
    db: Session = Depends(get_db)
):

    chat = ChatHistory(
        question=data["question"],
        answer=data["answer"],
        user_email=data.get(
            "user_email",
            "admin@nexusai.com"
        ),
        role=data.get(
            "role",
            "admin"
        ),
        document_name=data.get(
            "document_name",
            "Unknown"
        )
    )

    db.add(chat)
    db.commit()

    return {
        "message": "saved"
    }


@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):

    chats = (
        db.query(ChatHistory)
        .order_by(
            ChatHistory.timestamp.desc()
        )
        .all()
    )

    return [
        {
            "id": c.id,
            "question": c.question,
            "answer": c.answer,
            "user_email": c.user_email,
            "role": c.role,
            "document_name": c.document_name,
            "timestamp": str(c.timestamp)
        }
        for c in chats
    ]