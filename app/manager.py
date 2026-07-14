from app.scanner import BucketScanner
from app.remediation import BucketRemediator
from app.logs import LogAnalyzer
from app.report import IncidentReport


class CloudSecurityManager:

    def __init__(self):

        self.bucket_file = "data/buckets.json"
        self.log_file = "data/access_logs.json"

        self.scanner = BucketScanner(self.bucket_file)
        self.logs = LogAnalyzer(self.log_file)
        self.remediator = BucketRemediator(self.bucket_file)
        self.report = IncidentReport()

    def run(self):

        print("=" * 60)
        print("Cloud Storage Exposure Solution")
        print("=" * 60)

        public_buckets = self.scanner.find_public_buckets()

        if not public_buckets:
            print("\nNo public buckets found.")
            return

        print(f"\nFound {len(public_buckets)} public bucket(s).\n")

        for bucket in public_buckets:

            print(f"Bucket: {bucket['name']}")

            activity = self.logs.get_bucket_activity(bucket["name"])

            if activity:

                print("Activity:")

                for log in activity:

                    print(
                        f" {log['timestamp']} | "
                        f"{log['action']} | "
                        f"{log['file']} | "
                        f"{log['ip']}"
                    )

            else:

                print("No activity.")

            filename = self.report.create_report(
                bucket,
                activity
            )

            print(f"Report saved -> {filename}")

            print()

        fixed = self.remediator.remove_public_access()

        print("Buckets secured:")

        for bucket in fixed:
            print(f"✓ {bucket}")

        print("\nVerification Scan")

        remaining = self.scanner.find_public_buckets()

        if not remaining:
            print("SUCCESS: All buckets are private.")

        else:
            print("Some buckets are still public.")