from django.conf.urls import url
from .views import *

urlpatterns = [
    url('index/(\d+)*$', index),
    url('articles/(\S+)/(\d+)*$', article_category),
    url('detail/(\d+)*', article_detail),
    url('(\d+)*$', index),
]
