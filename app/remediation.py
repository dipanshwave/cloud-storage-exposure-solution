import json


class BucketRemediator:
    def __init__(self, bucket_file):
        self.bucket_file = bucket_file

    def load_buckets(self):
        with open(self.bucket_file, "r") as file:
            return json.load(file)

    def save_buckets(self, buckets):
        with open(self.bucket_file, "w") as file:
            json.dump(buckets, file, indent=4)

    def remove_public_access(self):
        buckets = self.load_buckets()

        fixed = []

        for bucket in buckets:
            if bucket["public"]:
                bucket["public"] = False
                fixed.append(bucket["name"])

        self.save_buckets(buckets)

        return fixed