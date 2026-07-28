from langchain_community.document_loaders import TextLoader

loader = TextLoader("projects\\06-Document-loaders\\python_notes.txt")

documents = loader.load()

# print(documents)

print(type(documents))
print(type(documents[0]))
print(documents[0].metadata["source"])

print(len(documents[0].page_content))