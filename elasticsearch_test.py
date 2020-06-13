import boto3
import re
import requests
import json
from requests_aws4auth import AWS4Auth

region = 'ap-southeast-2' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-plantly-es-cheap-my4i72dmshwihajjj2sbwqii3i.ap-southeast-2.es.amazonaws.com' # the Amazon ES domain, including https://

headers = { "Content-Type": "application/json" }

s3 = boto3.client('s3')

# Regular expressions used to parse some simple log lines
ip_pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
time_pattern = re.compile('\[(\d+\/\w\w\w\/\d\d\d\d:\d\d:\d\d:\d\d\s-\d\d\d\d)\]')
message_pattern = re.compile('\"(.+)\"')

type = "user_data"

_id =  'c0cb03a49a754a17b07b85c4d4f19039-test'

url = host + '/' + _id + '/' + type


query_body = {
  "query": {
        "match_all": {}
  }
}

r = requests.post(url, auth=awsauth, json=query_body, headers=headers)
        
print(r.text)