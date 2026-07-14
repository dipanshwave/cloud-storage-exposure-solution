from app.providers.aws.client import AWSClient


class AWSBucketScanner:

    def __init__(self):
        client = AWSClient()
        self.s3 = client.get_client()

    def list_buckets(self):
        response = self.s3.list_buckets()

        buckets = []

        for bucket in response["Buckets"]:
            buckets.append(bucket["Name"])

        return buckets