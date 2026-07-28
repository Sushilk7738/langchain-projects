from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("projects\\06-Document-loaders\\dl-curriculum.pdf")

document = loader.load()

# print(document)
print(len(document))

print(document[0].page_content)
print(document[0].metadata)