from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader("projects\\07-Text_splitters\\sample.txt")

documents = loader.load()

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap = 0
)

chunks = splitter.split_documents(documents)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-"*30)
    print(chunk.page_content)


