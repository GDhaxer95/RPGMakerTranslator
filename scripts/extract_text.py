import json
import os

def extract_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    texts = []
    if isinstance(data, list):  # For MapXXX.json or similar
        for event in data:
            if event and isinstance(event, dict):
                for key, value in event.items():
                    if isinstance(value, str):
                        texts.append(value)
    elif isinstance(data, dict):  # For Actors.json, etc.
        for key, value in data.items():
            if isinstance(value, str):
                texts.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        texts.append(item)
    return texts

def main():
    input_folder = "../www/data"
    output_file = "../data/extracted_text.txt"
    extracted_texts = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_folder, file_name)
            extracted_texts.extend(extract_text(file_path))

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(extracted_texts))

if __name__ == "__main__":
    main()
