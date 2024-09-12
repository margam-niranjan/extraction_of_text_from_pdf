import PyPDF2
import spacy

# Load the pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

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

def classify_text(text):
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Extract and classify entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

pdf_path = r"C:\Users\Niran\OneDrive\Desktop 1\py\minimizedpdf.pdf"

text = extract_text_from_pdf(pdf_path)
print("Extracted Text:\n", text)

# Classify the extracted text
entities = classify_text(text)
print("\nClassified Entities:")
for entity in entities:
    print(f"Entity: {entity[0]}, Label: {entity[1]}")
