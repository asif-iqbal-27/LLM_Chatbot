import os
from utils.text_chunking import chunk_text


input_dir = "data/extracted_text/"
output_dir = "data/chunked_text/"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each extracted text file
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_dir, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Chunk the text
        chunks = chunk_text(text, chunk_size=500)

        # Save chunks to a new file
        chunked_filename = filename.replace(".txt", "_chunks.txt")
        output_path = os.path.join(output_dir, chunked_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            for chunk in chunks:
                f.write(chunk + "\n\n")  
        
        print(f"✅ Chunked text saved: {output_path}")
