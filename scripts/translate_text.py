from deep_translator import GoogleTranslator, MyMemoryTranslator

def translate_text(input_file, output_file):
    # Initialize translators
    translators = [
        ("Google", GoogleTranslator(source="ja", target="en")),
        ("MyMemory", MyMemoryTranslator(source="ja-JP", target="en-US"))
    ]

    with open(input_file, "r", encoding="utf-8") as file:
        texts = file.readlines()

    translations = []
    for text in texts:
        text = text.strip()
        if not text:
            continue

        translated_texts = []
        for name, translator in translators:
            try:
                translated = translator.translate(text)
                translated_texts.append((name, translated))
            except Exception as e:
                print(f"Error with {name} Translator for '{text}': {e}")

        # Select the best translation (e.g., shortest length as a heuristic)
        if translated_texts:
            best_translation = min(translated_texts, key=lambda x: len(x[1]))[1]
            translations.append(best_translation)
        else:
            translations.append(text)  # Fallback to original text

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(translations))

if __name__ == "__main__":
    input_file = "./data/extracted_text.txt"
    output_file = "./data/translated_text.txt"
    translate_text(input_file, output_file)
