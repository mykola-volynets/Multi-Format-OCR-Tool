# 📄 Multi-Format OCR Tool

A simple, easy-to-use desktop application with a graphical interface for extracting text from images and documents (PNG, JPG, PDF, GIF, etc.). Powered by Google's Tesseract OCR, this tool is highly customizable and currently optimized for Ukrainian text, but can be easily adapted for any language.

## ✨ Features
- **Multi-Format Support:** Easily extract text from standard images (PNG, JPG) as well as PDFs and GIFs.
- **User-Friendly Interface:** A clean, straightforward GUI that requires no command-line knowledge to operate.
- **Highly Customizable:** Easily tweak the output file (e.g., text alignment, line density) with minimal code changes.
- **Easily Expandable:** Swap out the language model to extract text in almost any language.

---

## 🚀 Installation & Setup

To run this application, your system needs **Google's Tesseract** (for OCR) and **Poppler** (for PDF processing). Choose one of the setup methods below:

### Option 1: All-in-One Download (Recommended)
You can download the complete package, which already includes the script, Tesseract, Poppler, and the configured virtual environment.
👉 **[Download Complete Project from Google Drive](https://drive.google.com/drive/folders/1TxeEEYcwwRR-ZtDroUUie-_ylkRX97rc?usp=sharing)**

### Option 2: Manual Setup
If you prefer to set it up yourself from this repository:
1. Download the script (`main.py`).
2. **Download Tesseract:** Get the Windows installer [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe). 
3. Place the installed Tesseract folder directly next to `main.py` and rename the folder to exactly `TESSERACT`.
4. **Download Poppler:** Required for reading PDFs. Install it and ensure it is added to your system's PATH.

---

## 🌍 Changing the Language

By default, the tool is configured for **Ukrainian** (`ukr`). To change the OCR language:

1. Find and download your desired language data file (`.traineddata`) from the [Tesseract tessdata repository](https://github.com/tesseract-ocr/tessdata).
2. Place the downloaded file into your `TESSERACT/tessdata` folder.
3. Open `main.py` in your code editor, go to **Line 20**, and change `"ukr"` to your new language code (e.g., `"eng"`, `"fra"`, `"spa"`). Done!

---

## 📸 Screenshots & Examples

### App Interface
![Interface](https://github.com/user-attachments/assets/9bc55999-75bc-4e20-9c19-36e711ff37af)

### Example Extraction
Here is an example of the algorithm extracting text from a GIF file.

**Input (`test.gif`):** ![Input Image](https://github.com/user-attachments/assets/25e173b4-1867-47e7-96bf-7edb985cec8c)

**Output Result (Using default PSM):** ![Output Image](https://github.com/user-attachments/assets/a193eda3-b287-4dea-b25f-b7dfdd9b1633)
