def display_documents(documents):
    print(f"\nTotal Documents: {len(documents)}\n")

    for index, document in enumerate(documents, start=1):
        print(f"Document {index}")
        print("*"*40)
        print(f"Source: {document.metadata.get("source")}")
        print("Content: ")
        print(document.page_content[:200])
        print("\n")

    