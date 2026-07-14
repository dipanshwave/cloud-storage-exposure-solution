from app.aws.manager import AWSManager
from app.gcp.manager import GCPManager
from app.azure.manager import AzureManager


def select_cloud_provider():
    print("=" * 50)
    print("Cloud Storage Exposure Solution")
    print("=" * 50)
    print("Select Cloud Provider:\n")
    print("1. AWS")
    print("2. Google Cloud")
    print("3. Microsoft Azure")
    print()

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\nAWS Selected\n")
            return AWSManager()

        elif choice == "2":
            print("\nGoogle Cloud Selected\n")
            return GCPManager()

        elif choice == "3":
            print("\nMicrosoft Azure Selected\n")
            return AzureManager()

        else:
            print("Invalid choice. Please try again.\n")