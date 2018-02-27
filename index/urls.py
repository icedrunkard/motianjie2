from django.conf.urls import url
from .views import *

app_name = 'index'

urlpatterns = [
    url('', index, name='index'),
]
