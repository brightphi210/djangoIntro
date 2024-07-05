from django.shortcuts import render
from . models import *
# Create your views here.


def home(request):
    task = TodoTable.objects.all()
    print(task)
    return render(request, 'home.html', {'task':task})

