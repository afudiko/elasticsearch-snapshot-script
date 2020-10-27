import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://search-cxpsrch-es-kphb6smqgv7gllvkf32qgiquxe.ap-southeast-1.es.amazonaws.com/' # include https:// and trailing /
region = 'ap-southeast-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository

path = '_snapshot/my-snapshot-repo-name' # the Elasticsearch API endpoint
url = host + path

payload = {
  "type": "s3",
  "settings": {
    "bucket": "cxp-es-migration",
    # "endpoint": "us-east-1", # for us-east-1
    "region": "ap-southeast-1", # for all other regions
    "role_arn": "arn:aws:iam::517530806209:role/service-role/es.amazonaws.com/ServiceRoleForEs_elasticsearch_cxp_migration-8474acd3b8e9d224"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)