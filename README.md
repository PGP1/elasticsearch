# Elasticsearch
Description: contains tests, configs and setup instructions for our Elasticsearch Cluster

<h1> 1. Pre-Requistites </h1>

Dependencies
   - docker
   - python
   
We are no longer using a self-managed cluster so the only major pre-requisite is an AWS account to create an AWS managed Elasticsearch Cluster and docker or python to run the testing suite.

Alternatively you can host your own on a server (such as an EC2) by cloning this repo and running 

```docker-compose up```

while inside the directory to set up and run a simple 3 node + kibana cluster.

<h1> 2. Deployment </h1>

These instructions are for the AWS Elasticsearch managed service, if you wish to it with a self-hosted Elasticsearch instance using the docker-compose script then you can simply authenticate using http headers in requests.

### 2.1 Define your domain

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-gsg-create-domain.html

### 2.2 Configure your cluster

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html


### 2.3 Set up access via Cognito (will be used by Lambda functions)

https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html

### 2.4 Authentication

Authentication is done using the ```requests_aws4auth``` in conjunction with ```boto3``` or AWS Cognito.

To load credentials securely always use 

```credentials = boto3.Session().get_credentials()```
```awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)```

The ```awsauth``` variable can be used in place of any request requiring authorisation

<h1> 3 Testing </h1>

A set of integration tests have been cruited as a suite, subsequent tests depend on the previous test. There are two options to run these tests:

### 3.1 Docker

If you choose to run them using docker then simply use

```docker run --rm -it $(docker build -q .)``` with the Dockerfile in the test_suite/ directory.

This docker image will be deleted after running.

Otherwise follow the instructions below:

### 3.2 Testing script

Instal alll python dependencies

```pip3 install boto3```

```pip3 install elasticsearch```

```pip3 install re```

```pip3 install json```

```pip3 install requests```

```pip3 install requests_aws4auth```

 Run the testing script to print tests results to stdout

```sh run_tests.sh```

If all tests are executed succesfully the index created for testing will be deleted as part of the cleanup/final test.


