import pdfplumber
try:
   with pdfplumber.open('inputs/sample_invoice.pdf') as pdf:
        print(pdf.pages[0].extract_text())
except Exception as e:
       print(f"Error reading PDF: {e}")