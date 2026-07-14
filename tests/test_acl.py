from app.providers.aws.security import AWSSecurityAnalyzer

security = AWSSecurityAnalyzer()

bucket = "customer-documents"

public = security.is_bucket_public_acl(bucket)

print(f"Bucket: {bucket}")

if public:
    print("Status: PUBLIC")
else:
    print("Status: PRIVATE")