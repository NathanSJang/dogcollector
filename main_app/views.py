from django.shortcuts import render


# fake data
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


dogs = [
    Dog('Bell', 'Dobermann', 3),
    Dog('Shaw', 'Terrier', 7),
    Dog('Del', 'Poodle', 0),
]


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
