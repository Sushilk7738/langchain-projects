from langchain_community.document_loaders import DirectoryLoader, TextLoader


loader = DirectoryLoader(
    "projects\\06-Document-loaders\\Directory_loader\\data",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(len(documents))

for doc in documents:
    print(doc.metadata)


