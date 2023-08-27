import chromadb


chroma_client = chromadb.Client()


collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "this is a plumbing company",
        "we need a plumber asap",
        "kitchen sink has problems",
        "the living room is flooding",
        "bathroom needs cleaning immediately",
        "help! cleaner needed",
    ],
    metadatas=[
        {"source": "plumbing"},
        {"source": "plumbing"},
        {"source": "plumbing"},
        {"source": "plumbing"},
        {"source": "cleaning"},
        {"source": "cleaning"},
    ],
    ids=["id1", "id2", "id3", "id4", "id5", "id6"],
)


results = collection.query(
    query_texts=["need someone to install pipes in my kitchen"],
    n_results=2,
)

print(results)
