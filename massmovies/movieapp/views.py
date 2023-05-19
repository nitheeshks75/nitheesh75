from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import MoviesForm
from .models import Movies


# Create your views here.
def index(request):
    movie = Movies.objects.all()
    list = {
        'movie_list': movie
    }

    return render(request, 'index.html', list)


def detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)

    return render(request, "detail.html", {'movie': movie})


def Addmovie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        image = request.FILES['img']
        movie = Movies(name=name, desc=desc, year=year, image=image)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MoviesForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie': movie, 'form': form})
def delete(request, id):
    if request.method=='POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')