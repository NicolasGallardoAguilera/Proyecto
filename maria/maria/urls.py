from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('dashboard.urls'))
]
