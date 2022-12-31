from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from vyj.models import Post
from django.urls import reverse_lazy # para usar  nombres en las rutas
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from vyj.forms import UsuarioForm

#@login_required
def index(request):
    return render(request, "vyj/index.html",{})

class PostDetalle(DetailView):
    model = Post


class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("vyj-listar") # reverse lazy
    #success_url = "/vyj/listar"
    fields =  '__all__'

class PostListar(ListView):
    model = Post
  


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
    