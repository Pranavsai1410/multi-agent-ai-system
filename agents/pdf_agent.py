import pdfplumber
from memory.shared_memory import SharedMemory

class PDFAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, input_path, thread_id):
        try:
            with pdfplumber.open(input_path) as pdf:
                text = ""
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted

            # Extract key fields
            result = {}
            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if line.startswith("Invoice #"):
                    result["invoice_id"] = line.replace("Invoice #", "").strip()
                elif line.startswith("Total Amount:"):
                    result["amount"] = float(line.replace("Total Amount:", "").replace("$", "").strip())
                elif line.startswith("Date of Issue:"):
                    result["date"] = line.replace("Date of Issue:", "").strip()
                elif line.startswith("Email:"):
                    result["sender"] = line.replace("Email:", "").strip()

            # Save to memory
            context = self.memory.get_context(thread_id)
            context["extracted_fields"].update(result)
            self.memory.save_context(context["source"], context["type"], context["extracted_fields"])
            return result
        except Exception as e:
            print(f"Error processing PDF {input_path}: {e}")
            return {}