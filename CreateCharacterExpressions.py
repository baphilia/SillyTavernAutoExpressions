import os
import sys
import shutil
from PIL import Image
import base64
import json

# emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'neutral', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise']
emotions = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise']

def extract_name_from_metadata(file_path):
    with Image.open(file_path) as img:
        metadata = img.info
        for key, value in metadata.items():
            try:
                decoded_data = base64.b64decode(value)
                json_data = json.loads(decoded_data.decode("utf-8", errors="ignore"))
                return json_data["name"]
            except (base64.binascii.Error, json.JSONDecodeError):
                continue
    raise ValueError("Failed to extract name from the image file.")

if len(sys.argv) > 1:
    file_path = sys.argv[1]
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
                print(f"File {new_file_name} already exists, skipping...")
                continue
            shutil.copy2(file_path, new_file_path)
            print(f"Copy {i+1} created: {new_file_name}")

    except ValueError as error:
        print(error)
else:
    print("Please drag and drop a file onto this script to copy it with different filenames.")
