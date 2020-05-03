#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
import json, requests


HOST_ADRESS = "https://search-plantly-es-cheap-my4i72dmshwihajjj2sbwqii3i.ap-southeast-2.es.amazonaws.com"

INDEX_NAME = "c0cb03a49a754a17b07b85c4d4f19039-test"
	
user_request = "user-data"

es = Elasticsearch(hosts=[HOST_ADRESS])

# Take the user's parameters and put them into a
# Python dictionary structured as an Elasticsearch query:
query_body = {
  "query": {
        "match_all": {}
  }
}

# Pass the query dictionary to the 'body' parameter of the
# client's Search() method, and have it return results:
result = es.search(index=INDEX_NAME, body=query_body, size=999)
all_hits = result['hits']['hits']

# see how many "hits" it returned using the len() function
print ("total hits using 'size' param:", len(result["hits"]["hits"]))

# iterate the nested dictionaries inside the ["hits"]["hits"] list
for num, doc in enumerate(all_hits):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")

    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)

    # print a few spaces between each doc for readability
    print ("\n\n")

