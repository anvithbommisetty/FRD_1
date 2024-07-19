import re

def clean_transcript(transcript):
    # Remove timestamps
    transcript = re.sub(r'\b\d{1,2}:\d{2}(:\d{2})?\b', '', transcript)  # HH:MM:SS or MM:SS
        
    # Remove non-verbal cues (text within brackets)
    transcript = re.sub(r'\[.*?\]', '', transcript)
    
    # Normalize whitespace
    transcript = re.sub(r'\s+', ' ', transcript).strip()
    return transcript

def split_text(text, chunk_size):
    # Split text into words
    words = re.split(r'(\s+)', text)  # Keep the whitespace as separate elements
    
    chunks = []
    current_chunk = ""
    
    for word in words:
        if len(current_chunk) + len(word) > chunk_size:
            # If adding the next word exceeds the chunk size, store the current chunk
            chunks.append(current_chunk.strip())
            current_chunk = word
        else:
            current_chunk += word
    
    # Add the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def new_transcript(transcript):
    # Split the transcript into sentences
    cleaned_transcript = clean_transcript(transcript)
    
    sentences = re.split(r'(?<=[.!?]) +', cleaned_transcript)
    
    # Filter out three-word sentences
    filtered_sentences = [sentence for sentence in sentences if len(sentence.split()) > 3]
    
    # Join the remaining sentences back into a single string
    more_cleaned_transcript = ' '.join(filtered_sentences)
    chunks = split_text(more_cleaned_transcript, 6000)

    return chunks
