from app.providers.aws.client import AWSClient

client = AWSClient()
s3 = client.get_client()

bucket_name = "customer-documents"

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print("Error:", e)

print("\nCurrent Buckets:")

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print("-", bucket["Name"])