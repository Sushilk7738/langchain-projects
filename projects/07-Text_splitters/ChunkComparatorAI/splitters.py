from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter, 
    TokenTextSplitter,
    MarkdownHeaderTextSplitter,
    Language
)


def character_splitter(text, chunk_size=200, chunk_overlap=50):
    splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=chunk_size,
        chunk_overlap = chunk_overlap
    )
    
    return splitter.split_text(text)


def recursive_splitter(text, chunk_size=200, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap = chunk_overlap
    )
    
    return splitter.split_text(text)


def markdown_splitter(text):
    headers = [
        ("#", "H1"),
        ("##", "H2"),
        ("###", "H3"),
    ]
    
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers
    )
    
    return splitter.split_text(text)


def token_splitter(text, chunk_size=200, chunk_overlap=50):
    splitter = TokenTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)



def code_splitter(text, chunk_size=200, chunk_overlap=20):
    splitter = RecursiveCharacterTextSplitter.from_language(
        language= Language.PYTHON,
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )
    
    return splitter.split_text(text)