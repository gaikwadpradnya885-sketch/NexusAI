from fastapi import APIRouter
import os

router = APIRouter()

@router.delete("/documents/{filename}")
def delete_document(filename: str):

    file_path = os.path.join(
        "uploads",
        filename
    )

    if os.path.exists(file_path):

        os.remove(file_path)

        return {
            "message": "Document deleted"
        }

    return {
        "message": "Document not found"
    }