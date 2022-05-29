from pdf2image import convert_from_path

pdfs = r"/Users/kojimacbook/PycharmProjects/TOHacks/Koji Wong Resume.pdf"
pages = convert_from_path(pdfs)

i = 1
for page in pages:
    image_name = "Page" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i+1
