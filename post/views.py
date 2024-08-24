# from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Post
# para que la pagia siemprre vuelva a pricipal home
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):

    model= Post
    template_name= "home.html"
    
class DetailPageView(DetailView):
    
    model= Post
    template_name= "detail.html"
    
class CreatePageView(CreateView):
    model= Post
    template_name= "create.html"
    success_url= reverse_lazy("home")
    
    fields= ["titulo", "descripcion", "autor"]

class DeletePageView(DeleteView):
    
    model=Post
    template_name= "delete.html"
    success_url= reverse_lazy("home")
    
class UpdatePageView (UpdateView):
    template_name="update.html"
    model= Post
    fields= ["titulo", "descripcion"]
    success_url= reverse_lazy("home")