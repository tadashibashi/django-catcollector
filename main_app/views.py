from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import FeedingForm, CatForm
from .models import Cat, Toy


def home(request):
    return render(request, "cats/home.html", {})

def about(request):
    return render(request, "about.html", {})

def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = pk
        new_feeding.save()
    return redirect('main:cats_detail', pk = pk)


def detail(request, pk):
    cat = Cat.objects.get(id=pk)

    toys_have_ids = cat.toys.all().values_list('id')
    toys_not_have = Toy.objects.exclude(id__in=toys_have_ids)
    feeding_form = FeedingForm()
    return render(request, "cats/detail.html", {
        "feeding_form": feeding_form,
        "toys_not_have": toys_not_have,
        "cat": cat,
    })

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

    def get_form_class(self):
        return CatForm


class CatsUpdate(UpdateView):
    model = models.Cat
    fields = ["breed", "description", "age"]
    success_url = "/cats"

    def get_form_class(self):
        return CatForm

class CatsDelete(DeleteView):
    model = models.Cat
    success_url = "/cats"

def disassoc_toy(request, cat_id, toy_id):
    cat = get_object_or_404(Cat, id=cat_id)
    toy = get_object_or_404(Toy, id=toy_id)
    cat.toys.remove(toy)
    return redirect("main:cats_detail", pk=cat_id)

def assoc_toy(request, cat_id, toy_id):
    cat = get_object_or_404(Cat, id=cat_id)
    toy = get_object_or_404(Toy, id=toy_id)
    cat.toys.add(toy)
    return redirect("main:cats_detail", pk=cat_id)
