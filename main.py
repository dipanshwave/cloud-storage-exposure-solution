from core.menu import Menu
from app.providers.aws.controller import AWSController

aws = AWSController()

while True:

    provider = Menu.main_menu()

    if provider == "1":

        while True:

            choice = Menu.aws_menu()

            if choice == "1":
                aws.list_buckets()

            elif choice == "2":
                aws.scan_public_buckets()

            elif choice == "3":
                print("\nMake Bucket Public - Coming Soon\n")

            elif choice == "4":
                print("\nRemove Public Access - Coming Soon\n")

            elif choice == "5":
                print("\nUpload Test File - Coming Soon\n")

            elif choice == "6":
                print("\nList Bucket Objects - Coming Soon\n")

            elif choice == "7":
                print("\nAnalyze ACL - Coming Soon\n")

            elif choice == "8":
                print("\nAnalyze Bucket Policy - Coming Soon\n")

            elif choice == "9":
                print("\nGenerate Incident Report - Coming Soon\n")

            elif choice == "10":
                break

            elif choice == "11":
                print("\nGoodbye!")
                exit()

            else:
                print("\nInvalid choice.\n")

    elif provider == "2":
        print("\nGoogle Cloud support is coming soon.\n")

    elif provider == "3":
        print("\nMicrosoft Azure support is coming soon.\n")

    elif provider == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.\n")