import json
from memory.shared_memory import SharedMemory

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory
        self.target_schema = {
            "sender": str,
            "recipient": str,
            "amount": float,
            "date": str,
            "id": str
        }

    def validate_and_reformat(self, json_data):
        anomalies = []
        reformatted = {}

        for key, expected_type in self.target_schema.items():
            if key not in json_data:
                anomalies.append(f"Missing field: {key}")
                continue
            value = json_data[key]
            if not isinstance(value, expected_type):
                anomalies.append(f"Invalid type for {key}: expected {expected_type}, got {type(value)}")
            reformatted[key] = value

        return reformatted, anomalies

    def process(self, input_path, thread_id):
        with open(input_path, "r") as f:
            json_data = json.load(f)

        reformatted, anomalies = self.validate_and_reformat(json_data)
        context = self.memory.get_context(thread_id)
        context["extracted_fields"].update({"reformatted": reformatted, "anomalies": anomalies})
        self.memory.save_context(context["source"], context["type"], context["extracted_fields"])
        return reformatted, anomalies