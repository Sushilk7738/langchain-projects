from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python supports Object-Oriented Programming. It also supports Functional Programming. Python is widely used in AI.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=15
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 30)
    print(chunk)