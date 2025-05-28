import sqlite3
import json
from datetime import datetime
import uuid

class SharedMemory:
    def __init__(self, db_path="memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS context (
                    thread_id TEXT PRIMARY KEY,
                    source TEXT,
                    type TEXT,
                    timestamp TEXT,
                    extracted_fields TEXT
                )
            ''')
            conn.commit()

    def save_context(self, source, type, extracted_fields):
        thread_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO context (thread_id, source, type, timestamp, extracted_fields)
                VALUES (?, ?, ?, ?, ?)
            ''', (thread_id, source, type, timestamp, json.dumps(extracted_fields)))
            conn.commit()
        return thread_id

    def get_context(self, thread_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM context WHERE thread_id = ?', (thread_id,))
            result = cursor.fetchone()
            if result:
                return {
                    "thread_id": result[0],
                    "source": result[1],
                    "type": result[2],
                    "timestamp": result[3],
                    "extracted_fields": json.loads(result[4])
                }
        return None