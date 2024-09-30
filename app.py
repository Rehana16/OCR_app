import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Set the path for Tesseract executable if it's not in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # for Windows

# Function to highlight keywords in the text
def highlight_text(text, keyword):
    # Replace occurrences of the keyword with a highlighted version
    highlighted = text.replace(keyword, f"<mark>{keyword}</mark>")
    return highlighted

# Streamlit UI
st.title("OCR Processing for English and Hindi Text")
uploaded_file = st.file_uploader("Upload an image file for OCR processing.", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)

    # Convert the image to a format that OpenCV can work with
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Optional: Preprocess the image (convert to grayscale)
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    # Apply thresholding (optional)
    _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(thresh_image, lang='eng+hin')
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search functionality
    keyword = st.text_input("Enter keywords to search within the extracted text:")
    
    if keyword:
        # Check if the keyword is in the extracted text
        if keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{keyword}' found in the extracted text!")
            # Highlight the keyword in the text
            highlighted_text = highlight_text(extracted_text, keyword.lower())
            st.markdown("### Highlighted Text:")
            # Use st.markdown to render the highlighted text with unsafe HTML
            st.markdown(highlighted_text, unsafe_allow_html=True)
        else:
            st.error(f"Keyword '{keyword}' not found in the extracted text.")
