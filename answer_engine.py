from search_engine import search_document


def generate_answer(question):

    # 1. Check the question
    if not question or not question.strip():
        return {
            "question": question,
            "answer": "Please enter a question.",
            "pages": [],
            "passages": [],
            "similarity": 0,
            "sources": []
        }

    # 2. Search all documents
    results = search_document(question)

    # 3. Handle no search results
    if not results:
        return {
            "question": question,
            "answer": "I could not find relevant information in your documents.",
            "pages": [],
            "passages": [],
            "similarity": 0,
            "sources": []
        }

    # 4. Keep useful passages
    selected = []

    for result in results:

        text = result.get("text", "").strip()

        if len(text) >= 100:
            selected.append({
                "text": text,
                "source": result.get("source", "Unknown document"),
                "page": result.get("page", "Unknown"),
                "similarity": result.get("similarity", 0)
            })

    # 5. Handle empty passages
    if not selected:
        selected = results[:3]

    # 6. Prepare the answer
    answer = "\n\n".join(
        f"- {item['text']}" for item in selected
    )

    # 7. Collect page numbers
    pages = sorted(set(
        item["page"] for item in selected
    ))

    # 8. Collect document sources
    sources = sorted(set(
        item["source"] for item in selected
    ))

    # 9. Return the final response
    return {
        "question": question,
        "answer": answer,
        "pages": pages,
        "passages": selected,
        "similarity": results[0].get("similarity", 0),
        "sources": sources
    }


print("Answer engine loaded successfully.")