## Multi-Agent AI System

# Project Overview
This project is a multi-agent AI system that processes and analyzes emails, PDFs, and JSON files. It uses four AI agents to classify document types, identify intents, extract data, and store shared context in a SQLite database. The system is built with Python 3.12 and uses libraries like transformers, torch, PyPDF2, and pdfplumber.

# What the System Does
The system handles three input types:
- Emails (sample_email.txt): Extracts sender, intent (like like RFQ), urgency, and content.
- PDFs (sample_invoice.pdf): Extracts invoice details like ID, date, sender, and amount.
- JSON files (sample_json.json): Validates structure and extracts fields like sender, recipient, amount, and date.

# Four agents collaborate:
1. Classifier Agent: Identifies document type (Email, PDF, JSON) and intent.
2. Email Agent: Processes email files.
3. PDF Agent: Extracts data from PDF invoices.
4. JSON Agent: Validates and extracts JSON data.

A SQLite database (memory.db) stores context across agents, with each input assigned a unique thread ID.

# Prerequisites
You need:
- Python 3.12 (download from python.org)
- Git (download from git-scm.com)
- A code editor (like VS Code or Notepad)
- Optional: DB Browser for SQLite to view memory.db (download from sqlitebrowser.org)

# Setup Instructions
Follow these steps to run the project:
1. Clone the repository:
   git clone https://github.com/Pranavsai1410/multi-agent-ai-system.git
   cd multi-agent-ai-system
2. Create a virtual environment:
   python -m venv multi-agent-env
   On Windows, activate it:
   .\multi-agent-env\Scripts\activate
   On macOS/Linux:
   source multi-agent-env/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
   The requirements.txt includes:
   transformers==4.35.2
   torch==2.4.1
   PyPDF2==3.0.1
   pdfplumber
4. Run the system:
   python main.py
   To save output to a file:
   python main.py > output.log
5. View SQLite database (optional):
   Open memory.db in DB Browser for SQLite.
   Check the context table for processed data.

# File Structure
The project directory contains:
- agents/: Contains agent scripts
  - classifier_agent.py: Classifies document type and intent
  - email_agent.py: Processes email files
  - json_agent.py: Processes JSON files
  - pdf_agent.py: Processes PDF files
- inputs/: Input files
  - sample_email.txt: Sample email input
  - sample_invoice.pdf: Sample PDF invoice
  - sample_json.json: Sample JSON input
- memory/: Shared memory module
  - shared_memory.py: SQLite database management
- main.py: Main script to run the system
- test_pdf.py: Test script for PDF processing
- requirements.txt: Dependency list
- README.md: Project documentation
- .gitignore: Git ignore file
- output.log: Sample output log (generated after running)

# Demo
A demo video is available at: [Insert YouTube or Google Drive link after uploading].
The video shows:
- Running main.py to process sample_email.txt, sample_invoice.pdf, and sample_json.json.
- Console output with agent results.
- Viewing the context table in memory.db using DB Browser for SQLite.

# Sample Output
Example console output from running python main.py:
Processing inputs/sample_email.txt...
Classified as Email with intent RFQ (Thread ID: <uuid>)
Email Agent Result: {'sender': 'customer@example.com', 'intent': 'RFQ', 'urgency': 'Normal', 'content': 'Request for quotation for 100 units...'}
Context stored in memory.db

Processing inputs/sample_invoice.pdf...
Classified as PDF with intent Invoice (Thread ID: <uuid>)
PDF Agent Result: {'invoice_id': '12345', 'date': '2025-05-25', 'sender': 'vendor@example.com', 'amount': 5000.0}
Context stored in memory.db

Processing inputs/sample_json.json...
Classified as JSON with intent Invoice (Thread ID: <uuid>)
JSON Agent Result: {'sender': 'vendor@example.com', 'recipient': 'buyer@example.com', 'amount': 5000.0, 'date': '2025-05-28', 'id': 'INV12345'}, Anomalies: []
Context stored in memory.db

The full output is in output.log.

# Troubleshooting
- Large File Errors in Git:
  The multi-agent-env/ directory is excluded via .gitignore. Check for dependency files (like torch_cpu.dll):
  git ls-files | findstr "multi-agent-env"
  It should return nothing.
- Dependency Issues:
  Ensure Python 3.12 is active:
  python --version
  Update pip:
  pip install --upgrade pip
- PDF Processing Errors:
  Ensure sample_invoice.pdf is valid and under 100 MB.
  Test PDF processing:
  python test_pdf.py



