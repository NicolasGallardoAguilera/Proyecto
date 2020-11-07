from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import curso,alumno,usuario
from django.views.generic import TemplateView,ListView

# Create your views here.

class inicioview(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'app/inicio.html')

class cursos_profesor(LoginRequiredMixin,ListView):
    def get(self,request,**kwargs):
        return render(request,'app/cursos_profesor.html',{'cursos_profesor':curso.objects.filter(profesor_jefe=request.user.username)})


class alumnos_profesor(LoginRequiredMixin,ListView):
    def get(self,request,**kwargs):
        codigo= kwargs["id_curso"]
        return render(request,'app/alumnos_profesor.html',{'alumnos_profe':alumno.objects.filter(id_curso=codigo)})

class jefeutp_cursos(LoginRequiredMixin,ListView):
    def get(self, request,**kwargs):
        return render(request,'app/cursos_profesor.html',{'cursos_profesor':curso.objects.all()})

class director_profesores(LoginRequiredMixin,ListView):
    def get(self, request,**kwargs):
        return render(request,'app/trabajadores.html',{'usuarios_plataforma':usuario.objects.all()})


