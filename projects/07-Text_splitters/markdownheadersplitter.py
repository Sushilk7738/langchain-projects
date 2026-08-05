from langchain_text_splitters import MarkdownHeaderTextSplitter

headers = [
    ('#', 'Header 1'),
    ('##', 'Header 2'),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers
)


with open('projects\\07-Text_splitters\\sample.md', 'r', encoding="utf-8") as f:
    markdown = f.read()

chunks = splitter.split_text(markdown)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-"*30)
    print(chunk.page_content)
    print(chunk.metadata)


