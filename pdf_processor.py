import fitz
import os
import json

def process_pdfs():
    documents_folder = "documents"
    output_folder = "outputs"

    os.makedirs(output_folder, exist_ok=True)

    all_documents = []

    for filename in os.listdir(documents_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(documents_folder, filename)

            print("Processing:", filename)

            pdf = fitz.open(pdf_path)

            for page_number, page in enumerate(pdf):
                text = page.get_text()

                if text.strip():
                    all_documents.append({
                        "document": filename,
                        "page": page_number + 1,
                        "text": text
                    })

            pdf.close()

    output_path = os.path.join(output_folder, "all_documents.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(all_documents, file, ensure_ascii=False, indent=4)

    print("PDF processing completed!")
    print("Total pages extracted:", len(all_documents))
    print("Saved to:", output_path)

    return all_documents