import os
import requests

endpoint = os.getenv('AWS_CONTAINER_CREDENTIALS_RELATIVE_URI')
creds = requests.get(f'http://169.254.170.2{endpoint}').json()
print(f"export AWS_ACCESS_KEY_ID='{creds['AccessKeyId']}'")
print(f"export AWS_SECRET_ACCESS_KEY='{creds['SecretAccessKey']}'")