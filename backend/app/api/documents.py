from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/documents")
def get_documents():

    upload_folder = "uploads"

    if not os.path.exists(upload_folder):
        return []

    files = [
        file
        for file in os.listdir(upload_folder)
        if file.endswith(".pdf")
    ]

    return files