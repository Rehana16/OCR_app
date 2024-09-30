# OCR_app# OCR Processing for English and Hindi Text

This is a Streamlit application that performs Optical Character Recognition (OCR) on images containing English and Hindi text using Tesseract OCR. Users can upload images, and the application extracts text from those images and highlights specified keywords.

## Features

- Upload images in JPG, JPEG, or PNG formats.
- Extract text from images using Tesseract OCR.
- Search for keywords within the extracted text and highlight them.
- Supports both English and Hindi languages.

## Prerequisites

- Python 3.7+
- Tesseract OCR installed on your system. Download it from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).

### Set Up Tesseract

After installing Tesseract, ensure the executable path is correctly set in the code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # for Windows
```
### Requirements
- Python 3.7+
- streamlit
- pytesseract
- Pillow
- opencv-python
- numpy

Install dependencies using the following command:

```bash
pip install -r requirements.txt
```
## How to run the app
To run the Streamlit application, use the following command:
```bash
streamlit run app.py
```
Replace app.py with the name of your Python file if it's different.
