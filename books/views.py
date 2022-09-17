from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from books.models import Books


# def index(request):
#     template = loader.get_template("index.html")
#     return HttpResponse(template.render())

def index(request):
    books = Books.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'mybooks': books,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST["name"]
    genre = request.POST["genre"]
    price = request.POST["price"]
    obj = Books(name=name,genre=genre,price=int(price))
    obj.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    book=Books.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
  book = Books.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mybook': book,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    book = Books.objects.get(id=id)
    name = request.POST["name"]
    genre = request.POST["genre"]
    price = request.POST["price"]
    book.name = name
    book.genre = genre
    book.price = price
    book.save()
    return HttpResponseRedirect(reverse('index'))