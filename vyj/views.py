from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from vyj.models import Post
from django.urls import reverse_lazy # para usar  nombres en las rutas
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from vyj.forms import UsuarioForm
from vyj.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User

#@login_required
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "vyj/index.html", {"posts": posts})

def About(request):
    return render(request, 'vyj/about.html')

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post
  
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("vyj-listar") # reverse lazy
    #success_url = "/vyj/listar"
    fields =  '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("vyj-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("vyj-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('vyj-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('vyj-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('vyj-listar')


class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url =  reverse_lazy('vyj-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('vyj-listar')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("vyj-mensajes-listar")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("vyj-mensajes-listar")
    

