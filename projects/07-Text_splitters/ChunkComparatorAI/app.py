from pathlib import Path

from splitters import (
    character_splitter,
    recursive_splitter,
    token_splitter,
    markdown_splitter,
    code_splitter,
)

from analyzer import analyze_chunks


def main():

    base_dir = Path(__file__).parent

    file_name = input("Enter file name: ")
    file_path = base_dir / file_name

    if not file_path.exists():
        print("File not found.")
        return

    text = file_path.read_text(encoding="utf-8")

    extension = file_path.suffix.lower()

    print("\nChoose Chunking Strategy")
    print("1. Character Splitter")
    print("2. Recursive Splitter")
    print("3. Token Splitter")
    print("4. Markdown Splitter")
    print("5. Code Splitter")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        chunks = character_splitter(text)

    elif choice == "2":
        chunks = recursive_splitter(text)

    elif choice == "3":
        chunks = token_splitter(text)

    elif choice == "4":
        if extension != ".md":
            print("Markdown splitter only works with .md files.")
            return
        chunks = markdown_splitter(text)

    elif choice == "5":
        if extension != ".py":
            print("Code splitter only works with .py files.")
            return
        chunks = code_splitter(text)

    else:
        print("Invalid choice.")
        return

    analyze_chunks(chunks)


if __name__ == "__main__":
    main()