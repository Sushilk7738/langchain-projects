from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter

loader = PyPDFLoader("projects\\06-Document-loaders\\dl-curriculum.pdf")
documents = loader.load()

char_splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 50
)


token_splitter = TokenTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20
)

token_chunks = token_splitter.split_documents(documents)
char_chunks = char_splitter.split_documents(documents)

print("char chunks: ", len(char_chunks))
print("token chunks:" ,len(token_chunks))

# print(token_chunks[0].page_content)
# print(token_chunks[0].metadata)

