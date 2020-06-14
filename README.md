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

There are two options to run these tests:

If you choose to run them using docker then simply use

```docker run --rm -it $(docker build -q .)``` with the Dockerfile in the test_suite/ directory.

This docker image will be deleted after running.

Otherwise follow the instructions below:

3.1 Install testing dependecies

```pip3 install boto3```
```pip3 install elasticsearch```
```pip3 install re```
```pip3 install json```
```pip3 install requests```
```pip3 install requests_aws4auth```

3.2 Run the testing script to print tests results to stdout

```sh run_tests.sh`

If all tests are executed succesfully the index created for testing will be deleted as part of the cleanup/final test.


