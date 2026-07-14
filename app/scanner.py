import json
from pathlib import Path


class BucketScanner:
    def __init__(self, bucket_file):
        self.bucket_file = bucket_file

    def load_buckets(self):
        with open(self.bucket_file, "r") as file:
            return json.load(file)

    def find_public_buckets(self):
        buckets = self.load_buckets()

        public_buckets = [
            bucket for bucket in buckets if bucket["public"]
        ]

        return public_buckets