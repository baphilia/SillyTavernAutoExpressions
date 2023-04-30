import os
import sys
import shutil

# Define a list of emotions to use as filenames
emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'neutral', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise']

# Check if a file was dropped onto the script
if len(sys.argv) > 1:
    # Get the path of the dropped file
    file_path = sys.argv[1]
    # Get the filename and extension of the dropped file
    file_name, file_ext = os.path.splitext(file_path)
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Create copies of the dropped file with emotion filenames in the script directory
    for i, emotion in enumerate(emotions):
        new_file_name = f"{emotion}{file_ext}"
        new_file_path = os.path.join(script_dir, new_file_name)
        if os.path.exists(new_file_path):
            print(f"File {new_file_name} already exists, skipping...")
            continue
        shutil.copy2(file_path, new_file_path)
        print(f"Copy {i+1} created: {new_file_name}")
else:
    print("Please drag and drop a file onto this script to copy it with different filenames.")
