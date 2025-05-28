from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from agents.pdf_agent import PDFAgent
from memory.shared_memory import SharedMemory
import os

def main(input_file):
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)
    json_agent = JSONAgent(memory)
    email_agent = EmailAgent(memory)
    pdf_agent = PDFAgent(memory)

    format_type, intent, thread_id = classifier.process(input_file)
    if not format_type:
        return

    print(f"Classified as {format_type} with intent {intent} (Thread ID: {thread_id})")

    if format_type == "JSON":
        result, anomalies = json_agent.process(input_file, thread_id)
        print(f"JSON Agent Result: {result}, Anomalies: {anomalies}")
    elif format_type == "Email":
        result = email_agent.process(input_file, thread_id)
        print(f"Email Agent Result: {result}")
    elif format_type == "PDF":
        result = pdf_agent.process(input_file, thread_id)
        print(f"PDF Agent Result: {result}")

    context = memory.get_context(thread_id)
    print(f"Shared Memory Context: {context}")

if __name__ == "__main__":
    input_dir = "inputs"
    for input_file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, input_file)
        print(f"\nProcessing {input_path}...")
        main(input_path)