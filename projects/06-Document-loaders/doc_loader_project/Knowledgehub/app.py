from loaders import load_documents
from utils import display_documents


def main():
    documents = load_documents()
    display_documents(documents)


if __name__ == "__main__":
    main()