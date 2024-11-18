# RPG Maker MV Translation Tool

This project helps translate RPG Maker MV games from Japanese to English using Python scripts.

## Project Structure
- `www/data/`: The original game files.
- `data/`: Folder for extracted and translated text.
- `scripts/`: Python scripts for extraction, translation, and injection.

## How to Use
1. **Extract Text**:
   Run `extract_text.py` to extract all translatable text into `data/extracted_text.txt`.

   ```bash
   python scripts/extract_text.py
