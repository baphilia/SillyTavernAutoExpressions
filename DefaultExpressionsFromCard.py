import os
import sys
import shutil
import base64
import json
import struct
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'neutral', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise']
emotions = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise']

def get_character_name(chunk_data):
    prefix = b"chara\x00"
    length = len(prefix)
    decoded_data = base64.b64decode(chunk_data[length:]).decode('utf-8')
    json_data = json.loads(decoded_data)
    if "name" in json_data:
        return json_data["name"]
    return "Name not found"

def extract_name_from_metadata(file_path):
    # Fallback: manually parsing the PNG file
    with open(file_path, 'rb') as f:
        signature = f.read(8)
        if signature != b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
            raise ValueError("Not a valid PNG file.")

        while True:
            chunk_length_data = f.read(4)
            if not chunk_length_data:
                break

            chunk_length = struct.unpack('>I', chunk_length_data)[0]
            chunk_type = f.read(4).decode('ascii')
            chunk_data = f.read(chunk_length)
            f.read(4)  # Skip CRC
            
            if chunk_type in ['tEXt', 'zTXt', 'iTXt']:
                try:
                    return get_character_name(chunk_data)
                except Exception as e:
                    logging.warning(f"Error decoding base64 data (type: {chunk_type}, data: {chunk_data}): {e}")
                    continue

    raise ValueError("Failed to extract name from the image file.")

def process_file(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        extracted_name = extract_name_from_metadata(file_path)
        folder_path = os.path.join(script_dir, extracted_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for i, emotion in enumerate(emotions):
            new_file_name = f"{emotion}{file_ext}"
            new_file_path = os.path.join(folder_path, new_file_name)
            if os.path.exists(new_file_path):
                logging.info(f"File {new_file_name} already exists, skipping...")
                continue
            shutil.copy2(file_path, new_file_path)
            logging.info(f"Copy {i+1} created: {new_file_name}")

    except ValueError as error:
        logging.error(error)

def process_all_files_in_directory():
    for file_name in os.listdir():
        if file_name.endswith('.png'):
            logging.info(f"Processing file: {file_name}")
            process_file(file_name)


if len(sys.argv) > 1:
    if sys.argv[1] == "--all":
        process_all_files_in_directory()
    else:
        file_path = sys.argv[1]
        process_file(file_path)
else:
    logging.error("Please provide a file path as an argument or use the '--all' option to process all PNG files in the current directory.")
