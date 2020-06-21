from . import views
from django.conf.urls import url
from django.urls import path
from account.views import register


urlpatterns = [
        url(r'r', views.register, name='register'),
]
