# Elasticsearch
Tests, configs and setup instructions for our Elasticsearch Cluster

## 1 Pre-Requistites
We are no longer using a self-managed cluster so the only pre-requisite is an AWS account to create an AWS managed Elasticsearch Cluster

Alternatively you can host your own on a webserver (such as an EC2) by cloning this repo and running ``docker-compose up`` while inside the directory to run a simple 3 node + kibana cluster.

## 2 Deployment

2.1 Define your domain

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-gsg-create-domain.html

2.2 Configure your cluster

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html


2.3 Set up access via Cognito (will be used by Lambda functions)

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html

## 3 Testing

3.1 Send some test data to the new cluster

```curl -XPUT -u master-user:master-user-password domain-endpoint/movies/_doc/1 -d '{"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}' -H 'Content-Type: application/json'```

3.2 Then install pre-reqs for the testing script

``pip install elasticsearch``

and run it

``python3 elasticsearch_test``

You should see any data you've added printed to the console.


