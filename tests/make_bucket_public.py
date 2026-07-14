from app.providers.aws.client import AWSClient

client = AWSClient()
s3 = client.get_client()

bucket = "customer-documents"

s3.put_bucket_acl(
    Bucket=bucket,
    ACL="public-read"
)

print("Bucket is now PUBLIC.")