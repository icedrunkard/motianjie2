"""motianjie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.conf import settings
from django.views.static import serve as static_serve
import logreg.views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'logreg/',include('logreg.urls',namespace='logreg')),
    # url(r'logreg/register', logreg.views.register,name='register'),
    # url(r'logreg/login', logreg.views.login,name='login'),
    # url(r'logreg/logout', logreg.views.logout,name='logout'),
    url(r'schools/',include('schools.urls',namespace='schools')),
    url(r'',include('index.urls')),
]
if not settings.DEBUG:
    urlpatterns.insert(
        0,url(r'static/(.*)', static_serve, {'document_root': settings.STATIC_ROOT}),
    )