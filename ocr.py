from pdf2image import convert_from_path
from PIL import Image
from pytesseract import pytesseract

pdfs = r"C:\Users\Paula\TOHacks\Koji Wong Resume.pdf"
pages = convert_from_path(pdfs, 500)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i += 1

image_path = r"C:\Users\Paula\TOHacks\Page_1.jpg"
img = Image.open(image_path)
pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

text = pytesseract.image_to_string(img)
text_list = text.split('\n')
text_list = [i for i in text_list if i != '']
clean_text = ''.join(text_list)

print(clean_text)
