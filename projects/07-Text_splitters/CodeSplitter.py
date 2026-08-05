from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

with open("projects\\07-Text_splitters\\sample.py", 'r') as f:
    code = f.read()

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 20
)

chunks = splitter.split_text(code)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-"*30)
    print(chunk)


