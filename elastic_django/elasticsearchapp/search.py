from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch_dsl.connections import connections

from . import models
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

connections.create_connection()
client = Elasticsearch()

my_search = Search(using=client)


class PostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'post-index'

def bulk_indexing():
    # initialize the model to be indexed
    PostIndex.init()
    # pass Es to index the queryset from the model BlogPost as a generator
    bulk(client=client, actions=(blogpost.indexing() for blogpost in models.Post.objects.all().iterator()))

def search(query):
    query = my_search.query("multi_match", query=query, fields=['title', 'author', 'text'])
    response = query.execute()
    print(f'search.py response: {response}')
    return response