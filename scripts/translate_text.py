from googletrans import Translator

def main():
    input_file = "../data/extracted_text.txt"
    output_file = "../data/translated_text.txt"
    translator = Translator()

    with open(input_file, "r", encoding="utf-8") as file:
        texts = file.readlines()

    translations = [translator.translate(text.strip(), src="ja", dest="en").text for text in texts]

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(translations))

if __name__ == "__main__":
    main()
