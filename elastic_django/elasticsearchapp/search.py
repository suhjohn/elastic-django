from elasticsearch_dsl import DocType, Text, Date
from elasticsearch_dsl.connections import connections

from . import models
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

connections.create_connection()


class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Meta:
        index = 'blogpost-index'


def bulk_indexing():
    # initialize the model to be indexed
    BlogPostIndex.init()
    # pass Es to index the queryset from the model BlogPost as a generator
    client = Elasticsearch()
    bulk(client=client, actions=(blogpost.indexing() for blogpost in models.BlogPost.objects.all().iterator()))

