from django.conf.urls import url

from elasticsearchapp import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^search/$', views.search_post, name='search_post'),
]
