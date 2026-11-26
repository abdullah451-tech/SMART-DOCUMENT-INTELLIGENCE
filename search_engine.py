import json
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Load all document chunks
with open(
    "all_documents_chunks.json",
    "r",
    encoding="utf-8"
) as file:
    chunks = json.load(file)


# 2. Load all document embeddings
embeddings = np.load(
    "all_documents_embeddings.npy"
)


# 3. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 4. Validate the index
if len(chunks) != embeddings.shape[0]:
    raise ValueError(
        "Number of chunks and embeddings does not match."
    )


# 5. Search across all documents
def search_document(question):

    if not question or not question.strip():
        return []

    # Convert question into an embedding
    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    )

    # Calculate similarity
    similarities = cosine_similarity(
        question_embedding,
        embeddings
    )[0]

    # Get the 10 highest-scoring chunks
    top_indices = np.argsort(similarities)[-10:][::-1]

    results = []

    for index in top_indices:

        chunk = chunks[index]
        text = chunk["text"]

        # Skip very short passages
        if len(text.strip()) < 200:
            continue

        # Remove table-of-contents style passages
        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        short_lines = sum(
            1 for line in lines if len(line) < 60
        )

        if len(lines) >= 5 and short_lines / len(lines) > 0.65:
            continue

        # Store search result
        results.append({
            "source": chunk["source"],
            "page": chunk["page"],
            "text": text,
            "similarity": float(similarities[index])
        })

        if len(results) == 3:
            break

    return results


# 6. Confirm successful loading
print("Multi-document search engine loaded.")
print("Total chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print(
    "PDF sources:",
    sorted(set(chunk["source"] for chunk in chunks))
)
