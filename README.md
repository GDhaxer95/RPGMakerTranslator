# RPG Maker MV Translation Tool

This project helps translate RPG Maker MV games from Japanese to English using Python scripts.

## Project Structure
- `www/`: The original game files.
- `data/`: Folder for extracted and translated text.
- `scripts/`: Python scripts for extraction, translation, and injection.

## How to Use
1. **Extract Text**:
   Run `extract_text.py` to extract all translatable text into `data/extracted_text.txt`.

   ```bash
   python scripts/extract_text.py

2. **Translate Text**:
   Use `translate_text.py` to translate the text into English using Google Translate

   ```bash
   python scripts/translate_text.py

3. **Inject Translations**:
   Run `injext_text.py` to inject the translations back into JSON files.

   ```bash
   python scripts/translate_text.py
