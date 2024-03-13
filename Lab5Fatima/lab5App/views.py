from django.shortcuts import render


# Create your views here.

people = []

class Person:
    def __init__(self, username, password):
        
        username= self.username
        password= self.password


def add(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        person = Person(username=username, password=password)
        people.append(person)
    return render(request, 'add.html')

def defaultPath(request):
    
    return render(request, 'list.html', {'people': people})




