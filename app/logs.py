import json


class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def load_logs(self):
        with open(self.log_file, "r") as file:
            return json.load(file)

    def get_bucket_activity(self, bucket_name):
        logs = self.load_logs()

        return [
            log
            for log in logs
            if log["bucket"] == bucket_name
        ]