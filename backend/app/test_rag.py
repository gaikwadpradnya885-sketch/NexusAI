from app.services.rag_service import read_all_pdfs

text = read_all_pdfs()

print(text[:1000])