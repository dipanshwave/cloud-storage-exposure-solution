class Menu:

    @staticmethod
    def main_menu():

        print("\n" + "=" * 60)
        print(" Cloud Storage Exposure Solution ")
        print("=" * 60)

        print("1. AWS")
        print("2. Google Cloud")
        print("3. Azure")
        print("4. Exit")

        return input("\nSelect Provider: ")

    @staticmethod
    def aws_menu():

        print("\n" + "=" * 60)
        print(" AWS Security Dashboard ")
        print("=" * 60)

        print("1. List Buckets")
        print("2. Scan Public Buckets")
        print("3. Make Bucket Public")
        print("4. Remove Public Access")
        print("5. Upload Test File")
        print("6. List Objects")
        print("7. Analyze ACL")
        print("8. Analyze Bucket Policy")
        print("9. Generate Report")
        print("10. Back")
        print("11. Exit")

        return input("\nChoice: ")