from botocore.exceptions import ClientError
from app.providers.aws.client import AWSClient


class AWSSecurityAnalyzer:

    def __init__(self):
        client = AWSClient()
        self.s3 = client.get_client()

    def is_bucket_public_acl(self, bucket_name):

        try:
            acl = self.s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl["Grants"]:

                grantee = grant.get("Grantee", {})

                if (
                    grantee.get("Type") == "Group"
                    and "AllUsers" in grantee.get("URI", "")
                ):
                    return True

            return False

        except ClientError as e:
            print(f"Error checking ACL: {e}")
            return False