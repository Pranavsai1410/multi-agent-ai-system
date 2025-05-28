echo # Multi-Agent AI System > README.md
echo. >> README.md
echo A system that processes emails, JSON files, and PDFs using AI agents for classification and data extraction. >> README.md
echo. >> README.md
echo ## Setup Instructions >> README.md
echo 1. Install Python 3.12. >> README.md
echo 2. Create a virtual environment: >> README.md
echo    ```bash >> README.md
echo    python -m venv .\multi-agent-env >> README.md
echo    .\multi-agent-env\Scripts\activate >> README.md
echo    ``` >> README.md
echo 3. Install dependencies: >> README.md
echo    ```bash >> README.md
echo    pip install -r requirements.txt >> README.md
echo    ``` >> README.md
echo 4. Run: >> README.md
echo    ```bash >> README.md
echo    python main.py >> README.md
echo    ``` >> README.md
echo. >> README.md
echo ## Demo >> README.md
echo Watch the demo video: [Insert YouTube/Google Drive link here] >> README.md
echo. >> README.md
echo ## Sample Output >> README.md
echo ``` >> README.md
echo Processing inputs/sample_email.txt... >> README.md
echo Classified as Email with intent RFQ (Thread ID: <uuid>) >> README.md
echo Email Agent Result: {'sender': 'customer@example.com', 'intent': 'RFQ', 'urgency': 'Normal', 'content': '...'} >> README.md
echo ... >> README.md
echo. >> README.md
echo Processing inputs/sample_invoice.pdf... >> README.md
echo Classified as PDF with intent Invoice (Thread ID: <uuid>) >> README.md
echo PDF Agent Result: {'invoice_id': '12345', 'date': '2025-05-25', 'sender': 'vendor@example.com', 'amount': 5000.0} >> README.md
echo ... >> README.md
echo. >> README.md
echo Processing inputs/sample_json.json... >> README.md
echo Classified as JSON with intent Invoice (Thread ID: <uuid>) >> README.md
echo JSON Agent Result: {'sender': 'vendor@example.com', 'recipient': 'buyer@example.com', 'amount': 5000.0, 'date': '2025-05-28', 'id': 'INV12345'}, Anomalies: [] >> README.md
echo ... >> README.md
echo ``` >> README.md
