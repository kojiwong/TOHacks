from PIL import Image
from pytesseract import pytesseract, Output
import os
import spacy
import cv2
import streamlit as st
from pdf2image import convert_from_path
import main

pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def pdf_to_img(pdf_file):
    pages = convert_from_path(pdf_file, 500)
    image_name = "resume.jpg"
    pages[0].save(image_name, "JPEG")
    return image_name

def img_to_txt(image_name):
    img = Image.open(image_name)
    print('image is loaded')
    text = pytesseract.image_to_string(image_name)
    text_list = text.split('\n')
    text_list = [i for i in text_list if i != '']
    clean_text = ''.join(text_list)
    return clean_text

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a file", filenames)
    return os.path.join(folder_path, selected_filename)

if __name__ == '__main__':
    if st.checkbox("select a file in current directory"):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path')
        filename = file_selector(folder_path=folder_path)
        image = pdf_to_img(filename)
        st.write('You selected `%s`' % filename)
        suggestions = "Here are some suggestions"
        st.text(suggestions)
        st.text(main.prediction(img_to_txt(image)))
