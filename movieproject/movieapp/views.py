from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import MovieForm
from . models import movies
# Create your views h


def index(request):
    movie=movies.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})


def add(request):
    if request.method =='POST':
        name=request.POST.get('name',)
        details=request.POST.get('details',)
        image=request.FILES['image']
        movie=movies(name=name,details=details,image=image)
        movie.save()
    return render(request,'add.html')


def update(request,id):
    movie=movies.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')









    return render(request,'index.html',context)

