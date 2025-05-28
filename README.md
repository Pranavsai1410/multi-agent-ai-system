# Multi-Agent AI System

This project is a multi-agent AI system designed to process and analyze different types of documents—emails, PDFs, and JSON files. It uses four specialized AI agents to classify document formats, identify intents, extract relevant data, and store shared context in a SQLite database. The system is built with Python 3.12 and leverages libraries like `transformers`, `torch`, `PyPDF2`, and `pdfplumber`.

## Project Overview

The system processes three types of input files:
- **Emails** (`sample_email.txt`): Extracts sender, intent (e.g., RFQ), urgency, and content.
- **PDFs** (`sample_invoice.pdf`): Extracts invoice details like ID, date, sender, and amount.
- **JSON files** (`sample_json.json`): Validates structure and extracts fields like sender, recipient, amount, and date.

Four agents work collaboratively:
1. **Classifier Agent**: Identifies the document type (Email, PDF, JSON) and intent.
2. **Email Agent**: Processes email files for key information.
3. **PDF Agent**: Extracts data from PDF invoices.
4. **JSON Agent**: Validates and extracts data from JSON files.

A shared SQLite database (`memory.db`) stores context across agents, enabling coordinated processing. Each input is assigned a unique thread ID for tracking.

## Prerequisites

Before running the system, ensure you have the following installed:
- Python 3.12 (download from [python.org](https://www.python.org/downloads/))
- Git (download from [git-scm.com](https://git-scm.com/))
- A code editor (e.g., VS Code, Notepad)
- (Optional) DB Browser for SQLite to view `memory.db` (download from [sqlitebrowser.org](https://sqlitebrowser.org/))

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pranavsai1410/multi-agent-ai-system.git
   cd multi-agent-ai-system


Create a Virtual Environment:
python -m venv multi-agent-env


On Windows, activate it:.\multi-agent-env\Scripts\activate


On macOS/Linux:source multi-agent-env/bin/activate




Install Dependencies:Ensure you’re in the project directory, then run:
pip install -r requirements.txt

The requirements.txt includes:
transformers==4.35.2
torch==2.4.1
PyPDF2==3.0.1
pdfplumber


Run the System:Execute the main script:
python main.py

This processes the input files in the inputs/ directory and generates output in the console. To save output to a file:
python main.py > output.log


View SQLite Database (Optional):

Open memory.db in DB Browser for SQLite.
Check the context table for stored data from processed inputs.



File Structure
The project directory is organized as follows:
multi-agent-ai-system/
├── agents/                     # Agent scripts
│   ├── classifier_agent.py     # Classifies document type and intent
│   ├── email_agent.py          # Processes email files
│   ├── json_agent.py           # Processes JSON files
│   ├── pdf_agent.py            # Processes PDF files
├── inputs/                     # Input files
│   ├── sample_email.txt        # Sample email input
│   ├── sample_invoice.pdf      # Sample PDF invoice
│   ├── sample_json.json        # Sample JSON input
├── memory/                     # Shared memory module
│   ├── shared_memory.py        # SQLite database management
├── main.py                     # Main script to run the system
├── test_pdf.py                 # Test script for PDF processing
├── requirements.txt            # Dependency list
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── output.log                  # Sample output log (generated after running)

Demo
A demo video showcasing the system’s functionality is available here: [Insert YouTube or Google Drive link after uploading].
The video demonstrates:

Running main.py to process sample_email.txt, sample_invoice.pdf, and sample_json.json.
Console output showing agent results.
Viewing the context table in memory.db using DB Browser for SQLite.

Sample Output
Below is an example of the console output when running python main.py:
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

The full output is saved in output.log.
Troubleshooting

Large File Errors in Git:
The multi-agent-env/ directory (virtual environment) is excluded via .gitignore. If you encounter large file errors, ensure no dependency files (e.g., torch_cpu.dll) are tracked:git ls-files | findstr "multi-agent-env"


Should return nothing.




Dependency Issues:
If pip install -r requirements.txt fails, ensure Python 3.12 is active:python --version


Update pip:pip install --upgrade pip




PDF Processing Errors:
Ensure sample_invoice.pdf is valid and <100 MB.
Test PDF processing:python test_pdf.py





Submission Details
This project was developed for a submission to FlowBit AI. Submission details:

GitHub Repository: https://github.com/Pranavsai1410/multi-agent-ai-system
Demo Video: [Insert link after uploading]
Output Log: Available in output.log
Contact: Submitted to soham.shah@flowbitai.com by [Your Name] on or before June 1, 2025.

Acknowledgments

Built with Python 3.12 and open-source libraries.
