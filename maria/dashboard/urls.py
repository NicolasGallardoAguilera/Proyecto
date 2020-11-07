from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from dashboard.views import inicioview,cursos_profesor,alumnos_profesor,jefeutp_cursos,director_profesores
from django.contrib.auth.views import logout_then_login,LoginView

urlpatterns = [
    re_path('^$',inicioview.as_view(),name="home"),
    re_path('accounts/', include('accounts.urls')),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path('logout/',logout_then_login, name= 'logout'),
    re_path('profesor/cursos',cursos_profesor.as_view(),name='profesorcursos'),
    re_path('profesor/alumnos/(?P<id_curso>[\w\.]+)',alumnos_profesor.as_view(), name='profesoralumnos'),
    re_path('jefeutp/cursos',jefeutp_cursos.as_view(),name='jefeutpcursos'),
    re_path('director/trabajadores',director_profesores.as_view(),name='directorpersonal'),
]