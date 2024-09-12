import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

pdf_path = pdf_path = r"C:\Users\pooja\OneDrive\Desktop\New folder\extraction_of_text_from_pdf\WT notes.pdf"

text = extract_text_from_pdf(pdf_path)
print(text)
