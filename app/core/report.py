from datetime import datetime


class IncidentReport:

    def __init__(self, report_folder="reports"):
        self.report_folder = report_folder

    def create_report(self, bucket, activity):

        filename = (
            f"{self.report_folder}/"
            f"{bucket['name']}_report.txt"
        )

        with open(filename, "w") as report:

            report.write("Cloud Security Incident Report\n")
            report.write("=" * 40 + "\n\n")

            report.write(f"Bucket: {bucket['name']}\n")
            report.write(f"Owner: {bucket['owner']}\n")
            report.write(f"Region: {bucket['region']}\n\n")

            report.write(f"Generated: {datetime.now()}\n\n")

            report.write("Activity\n")
            report.write("-" * 20 + "\n")

            if not activity:
                report.write("No activity found.\n")
            else:
                for log in activity:

                    report.write(
                        f"{log['timestamp']} | "
                        f"{log['action']} | "
                        f"{log['file']} | "
                        f"{log['ip']}\n"
                    )

            report.write("\n")

            report.write("Remediation\n")
            report.write("-" * 20 + "\n")

            report.write(
                "Public access removed successfully.\n"
            )

        return filename