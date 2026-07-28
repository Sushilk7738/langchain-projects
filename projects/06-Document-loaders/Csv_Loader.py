from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(
    file_path="projects\\06-Document-loaders\\emp.csv"
)

documents = loader.load()

print(documents)

print(len(documents))

print(type(documents[0].page_content))
print(documents[0].page_content)
print(documents[0].metadata)