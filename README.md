# Multi-Agent AI System

A system that processes emails, JSON files, and PDFs using AI agents for classification and data extraction.

---

## 🛠️ Setup Instructions

1. **Install Python 3.12**  
   Ensure Python is installed and added to your system PATH.

2. **Create a virtual environment:**
   python -m venv .\multi-agent-env
   .\multi-agent-env\Scripts\activate
   
# Install dependencies:
pip install -r requirements.txt
Run the main program:
python main.py
▶️ Demo
Watch the demo video: [Insert YouTube/Google Drive link here]

#🧪 Sample Output

Processing inputs/sample_email.txt...
Classifier output for text 'From: customer@example.com...'
Classified as Email with intent RFQ (Thread ID: <uuid>)
Email Agent Result: {'sender': 'customer@example.com', 'intent': 'RFQ', 'urgency': 'Normal', 'content': '...'}

Processing inputs/sample_invoice.pdf...
Extracted PDF text: Invoice #12345...
Classified as PDF with intent Invoice (Thread ID: <uuid>)
PDF Agent Result: {'invoice_id': '12345', 'date': '2025-05-25', 'sender': 'vendor@example.com', 'amount': 5000.0}

Processing inputs/sample_json.json...
Classified as JSON with intent Invoice (Thread ID: <uuid>)
JSON Agent Result: {'sender': 'vendor@example.com', 'recipient': 'buyer@example.com', 'amount': 5000.0, 'date': '2025-05-28', 'id': 'INV12345'}, Anomalies: []


📁 Directory Structure

├── main.py
├── agents/
│   ├── email_agent.py
│   ├── pdf_agent.py
│   └── json_agent.py
├── classifier/
│   └── classify.py
├── shared_memory/
│   └── memory.py
├── inputs/
│   ├── sample_email.txt
│   ├── sample_invoice.pdf
│   └── sample_json.json
├── requirements.txt
└── README.md

📌 Notes
Thread IDs are dynamically generated for traceability.
Shared memory stores results with timestamps and source metadata.
Easily extendable to support other formats or agent types.
