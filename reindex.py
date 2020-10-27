import boto3
import requests
import time
import json
import thread
from requests_aws4auth import AWS4Auth

default_repo_name = "tvlk-repo"


role = requests.get("http://169.254.169.254/latest/meta-data/iam/security-credentials/").text
role = requests.get("http://169.254.169.254/latest/meta-data/iam/security-credentials/"+role)
credentials = boto3.Session().get_credentials()
aws4auth = AWS4Auth(credentials.access_key, credentials.secret_key, "ap-southeast-1", 'es', session_token=credentials.token)

url = 'https://vpc-cxpsrch-omni-e559301ac46ea1-oxyp352i6hjoxuwxjk3oho5fba.ap-southeast-1.es.amazonaws.com/_reindex'
payload = {"source": {"index": "restoreda_.kibana"},"dest": {"index": ".kibana"}}
payload = json.dumps(payload)

host = 'https://vpc-cxpsrch-omni-e559301ac46ea1-oxyp352i6hjoxuwxjk3oho5fba.ap-southeast-1.es.amazonaws.com/_cat/indices'

requests.put(host, auth=aws4auth, headers={"Content-Type": "application/json"})
