from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
]

