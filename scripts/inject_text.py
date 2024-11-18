import json
import os

def inject_translations(file_path, translations):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    idx = 0
    if isinstance(data, list):  # For MapXXX.json or similar
        for event in data:
            if event and isinstance(event, dict):
                for key, value in event.items():
                    if isinstance(value, str) and idx < len(translations):
                        event[key] = translations[idx]
                        idx += 1
    elif isinstance(data, dict):  # For Actors.json, etc.
        for key, value in data.items():
            if isinstance(value, str) and idx < len(translations):
                data[key] = translations[idx]
                idx += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    input_folder = "../www/data"
    translations_file = "../data/translated_text.txt"

    with open(translations_file, "r", encoding="utf-8") as file:
        translations = file.readlines()

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_folder, file_name)
            inject_translations(file_path, translations)

if __name__ == "__main__":
    main()
