def analyze_chunks(chunks):
    if not chunks:
        print("No chunks found.")
        return
    
    print("\n" + "=" * 50)
    print("CHUNK ANALYSIS")
    print("="*50)
    
    print(f"Total chunks: {len(chunks)}")

    sizes = []

    for chunk in chunks:
        if hasattr(chunk, "page_content"):
            sizes.append(len(chunk.page_content))
        else:
            sizes.append(len(chunk))

    average_size = sum(sizes) / len(sizes)
    
    print(f"Average Chunk Size: {average_size:.2f} chars")

    print(f"Largest Chunk: {max(sizes)} chars")

    print(f"Smallest Chunk: {min(sizes)} chars")