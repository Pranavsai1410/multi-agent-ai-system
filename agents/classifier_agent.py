from transformers import pipeline
import json
import os
import pdfplumber
from memory.shared_memory import SharedMemory

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def classify_format(self, input_path):
        ext = os.path.splitext(input_path)[1].lower()
        if ext == ".pdf":
            return "PDF"
        elif ext == ".json":
            return "JSON"
        elif ext == ".txt":
            return "Email"
        return None

    def extract_pdf_text(self, pdf_path):
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted
            print(f"Extracted PDF text: {text[:200]}...")  # Debug print
            return text
        except Exception as e:
            print(f"Error reading PDF {pdf_path}: {e}")
            return ""

    def classify_intent(self, text, format_type):
        if not text:
            return "Unknown"

        # Keyword-based classification for JSON and PDF
        if format_type in ["JSON", "PDF"]:
            lower_text = text.lower()
            invoice_keywords = ["invoice", "amount", "payment", "due date"]
            if any(keyword in lower_text for keyword in invoice_keywords):
                print(f"Intent classified as Invoice due to keywords: {invoice_keywords}")  # Debug print
                return "Invoice"
            if any(keyword in lower_text for keyword in ["regulation", "compliance"]):
                print(f"Intent classified as Regulation due to keywords: ['regulation', 'compliance']")  # Debug print
                return "Regulation"

        # Fallback to transformer-based classification
        result = self.classifier(text[:512])[0]
        print(f"Classifier output for text '{text[:100]}...': {result}")
        label = result["label"]
        intent_map = {"POSITIVE": "RFQ", "NEGATIVE": "Complaint", "NEUTRAL": "Invoice"}
        return intent_map.get(label, "Regulation")

    def process(self, input_path):
        format_type = self.classify_format(input_path)
        if not format_type:
            print(f"Invalid input format for {input_path}")
            return None, None, None

        if format_type == "PDF":
            content = self.extract_pdf_text(input_path)
        elif format_type == "JSON":
            with open(input_path, "r") as f:
                content = json.load(f)
                content = json.dumps(content)
        else:  # Email
            with open(input_path, "r") as f:
                content = f.read()

        intent = self.classify_intent(content, format_type)
        thread_id = self.memory.save_context(input_path, format_type + "+" + intent, {"format": format_type, "intent": intent})
        return format_type, intent, thread_id