from django.conf.urls import url
from .views import *

app_name = 'logreg'

urlpatterns = [
    url('login/', login, name='login'),
    url('logout/', logout, name='logout'),
    url('register/', register, name='register'),
    url('share/', share, name='share'),
]
