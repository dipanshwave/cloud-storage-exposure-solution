from app.providers.aws.scanner import AWSBucketScanner

print("Starting scanner...")

scanner = AWSBucketScanner()

print("Scanner initialized.")

buckets = scanner.list_buckets()

print("Buckets returned:", buckets)

if not buckets:
    print("No buckets found.")
else:
    print("\nBuckets:")
    for bucket in buckets:
        print(bucket)