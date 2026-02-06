def load_pdf(file_path):
    """
    Load a PDF file and extract its text content.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content from the PDF.
    """
    from pypdf import PdfReader

    text_content = []
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text_content.append(page.extract_text())
    
    return "\n".join(text_content)

def load_markdown(file_path):
    """
    Load a Markdown file and extract its text content.

    Args:
        file_path (str): The path to the Markdown file.     
    Returns:
        str: The extracted text content from the Markdown file.

    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()