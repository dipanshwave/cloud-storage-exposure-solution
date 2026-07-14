from app.providers.aws.scanner import AWSBucketScanner
from app.providers.aws.security import AWSSecurityAnalyzer


class AWSController:

    def __init__(self):

        self.scanner = AWSBucketScanner()
        self.security = AWSSecurityAnalyzer()

    def list_buckets(self):

        buckets = self.scanner.list_buckets()

        print("\nBuckets Found")
        print("-" * 40)

        if not buckets:
            print("No buckets found.\n")
            return

        for bucket in buckets:
            print(bucket)

        print()

    def scan_public_buckets(self):

        buckets = self.scanner.list_buckets()

        if not buckets:
            print("\nNo buckets found.\n")
            return

        print("\nScanning buckets...\n")

        for bucket in buckets:

            public = self.security.is_bucket_public_acl(bucket)

            print(f"Bucket : {bucket}")

            if public:
                print("Status : PUBLIC")
                print("Risk   : HIGH")
                print("Reason : Public ACL")

            else:
                print("Status : PRIVATE")

            print("-" * 40)