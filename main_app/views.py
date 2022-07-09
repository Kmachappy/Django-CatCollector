from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Cat
# Faux cat data - database simulation
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4),
#     Cat('Mimi', 'california tabby', 'cat from arizona', 4),
#     Cat('Momo', 'california tabby mix', 'she likes to bring mice', 2),
#     Cat('Lalo', 'california tabby mix', 'chonky boy who loves to ear',2),
#     Cat('Sasuke', 'black california tabbi mix', 'best cat ever i miss her', 2),
# ]



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    # return HttpResponse("<h1>About ༼つ ் ▽ ் ༽つ</h1>")
    return render(request, 'about.html')

def cats_index(request):
    # coming from the import data base than before when it was being hardcoded
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats':cats})

def cats_detail(request, cat_id):
    # get the individual cat
    cat = Cat.objects.get(id=cat_id)
    #  render template, pass it the cat
    return render(request, 'cats/detail.html', {'cat':cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'
    # fields = ['name', 'breed','description','age']

class CatUpdate(UpdateView):
    model = Cat
    # let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed','description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'