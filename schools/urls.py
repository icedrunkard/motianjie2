from django.conf.urls import url
from .views import *
app_name = 'schools'

urlpatterns = [
    url('(\d+)/departments/(\d+)', tutors, name='tutors'),
    url('(\d+)/$', dpts, name='dpts'),
    url('', schools, name='schools'),

]
