from langchain_community.document_loaders import (
    DirectoryLoader, 
    TextLoader,
    CSVLoader,
    PyPDFLoader,
)

from pathlib import Path



DATA_DIR = Path("projects\doc_loader_project\Knowledgehub\data")

LOADERS =  {
    ".txt": TextLoader,
    ".pdf": PyPDFLoader,
    ".csv": CSVLoader,
}

def load_documents():
    documents = []
    
    
    for extention,loader_cls in LOADERS.items():
        loader = DirectoryLoader(
            DATA_DIR,
            glob=f"**/*{extention}",
            loader_cls=loader_cls,
        )

        documents.extend(loader.load())
        
    return documents

