from django.shortcuts import render, redirect
from . models import *
# Create your views here.


def home(request):
    # getting is used get data from your database
    alltask = TodoTable.objects.all().order_by('-id')

    # POST = is used to send a request to your server
    if request.method == 'POST':
        fTitle = request.POST.get('title')
        fDescription = request.POST.get('description')

        print(fTitle)
        print(fDescription)

        task = TodoTable.objects.create(title=fTitle, description=fDescription)
        task.save()
    return render(request, 'home.html', {'tasks' : alltask})



# update function
def updateTask(request, pk):
    task = TodoTable.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('newtitle')
        description = request.POST.get('description')
        task.title = title
        print(title)
        task.description = description  
        task.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task})

# delete function 
def deleteTask(request, pk):
    task = TodoTable.objects.get(pk=pk)
    task.delete()
    return redirect('/')



