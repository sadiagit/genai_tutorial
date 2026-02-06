import tiktoken
def chunk_text(text, chunk_size=800, overlap=200):
    """
    Splits the input text into chunks of specified size with a given overlap.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0   
    tokens = tiktoken.get_encoding("cl100k_base").encode(text)

    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_tokens = tokens[start:end]
        
        # Decode tokens back to text, so embedding can use the original text for each chunk
        chunk_text = tiktoken.get_encoding("cl100k_base").decode(chunk_tokens)

        chunks.append(chunk_text)
        start += chunk_size - overlap

    return chunks