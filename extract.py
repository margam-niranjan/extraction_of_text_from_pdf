import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text() or ""
    except FileNotFoundError:
        print(f"The file at {pdf_path} was not found.")
    except PyPDF2.errors.PdfReadError:
        print(f"Error reading the PDF file at {pdf_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return text

pdf_path = r"C:\Users\Niran\OneDrive\Desktop 1\py\B.Tech-II-year-CSE-R20-syllabus-1-1.pdf"

text = extract_text_from_pdf(pdf_path)
print(text)
