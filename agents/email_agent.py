from transformers import pipeline
from memory.shared_memory import SharedMemory

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory
        self.sentiment_analyzer = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def extract_info(self, email_content):
        lines = email_content.split("\n")
        sender = None
        for line in lines:
            if line.startswith("From:"):
                sender = line.replace("From:", "").strip()
                break

        sentiment = self.sentiment_analyzer(email_content[:512])[0]
        urgency = "High" if sentiment["label"] == "NEGATIVE" and sentiment["score"] > 0.9 else "Normal"
        intent = "Complaint" if sentiment["label"] == "NEGATIVE" else "RFQ"

        return {
            "sender": sender or "Unknown",
            "intent": intent,
            "urgency": urgency,
            "content": email_content[:200]  # Truncated for CRM
        }

    def process(self, input_path, thread_id):
        with open(input_path, "r") as f:
            email_content = f.read()

        extracted = self.extract_info(email_content)
        context = self.memory.get_context(thread_id)
        context["extracted_fields"].update(extracted)
        self.memory.save_context(context["source"], context["type"], context["extracted_fields"])
        return extracted