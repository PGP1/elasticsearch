from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

host = 'search-plantly-es-cheap-my4i72dmshwihajjj2sbwqii3i.ap-southeast-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
region = 'ap-southeast-2' # e.g. us-west-1

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

index = "testing_data"

# delete the testing index
try:
    es.indices.delete(index=index)
    print("Successfully deleted:", index)
except Exception as error:
    print('indices.delete error:', error, 'for index:', index)
