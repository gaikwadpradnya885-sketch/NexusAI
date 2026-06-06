import os
from langchain_community.document_loaders import PyPDFLoader


def read_pdf(file_path):
    loader = PyPDFLoader(file_path)

    documents = loader.load()

    text = ""

    for doc in documents:
        text += doc.page_content + "\n"

    return text


def read_all_pdfs():

    upload_folder = "uploads"

    all_text = ""

    if not os.path.exists(upload_folder):
        return "Uploads folder not found."

    for file in os.listdir(upload_folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                upload_folder,
                file
            )

            try:
                text = read_pdf(pdf_path)

                all_text += (
                    f"\n\n===== {file} =====\n\n"
                )

                all_text += text

            except Exception as e:

                print(
                    f"Error reading {file}: {e}"
                )

    return all_text


def search_pdf(question):

    text = read_all_pdfs()

    if not text:
        return "No documents found."

    # Temporary MVP search
    question = question.lower()

    if "leave" in question:
        return text[:1000]

    if "policy" in question:
        return text[:1000]

    if "employee" in question:
        return text[:1000]

    return text[:1000]