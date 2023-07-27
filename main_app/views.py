from . import models
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

class CatsDetail(DetailView):
    model = models.Cat
    template_name = "cats/detail.html"

class CatsList(ListView):
    model = models.Cat
    template_name = "cats/index.html"
    context_object_name = "cats"

    def get_queryset(self):
        return get_list_or_404(models.Cat)

class CatsCreate(CreateView):
    model = models.Cat
    fields = "__all__"
    success_url = '/cats'

class CatsUpdate(UpdateView):
    model = models.Cat
    fields = ["breed", "description", "age"]
    success_url = "/cats"

class CatsDelete(DeleteView):
    model = models.Cat
    success_url = "/cats"
