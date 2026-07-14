import boto3


class AWSClient:

    def __init__(self):

        self.s3 = boto3.client(
            "s3",
            endpoint_url="http://localhost:4566",
            aws_access_key_id="test",
            aws_secret_access_key="test",
            region_name="us-east-1"
        )

    def get_client(self):
        return self.s3