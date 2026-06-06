from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(Text)

    answer = Column(Text)

    user_email = Column(String)

    role = Column(String)

    document_name = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )