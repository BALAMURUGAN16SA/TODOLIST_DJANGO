from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List, Task
# Create your views here.
def home(response):
    return render(response, "content/home.html", {})

@login_required
def overview(response):
    user = response.user
    listCount = taskCount = 0
    listObj = List.objects.filter(user = user)
    for obj1 in listObj:
        listCount += 1
        taskObj = Task.objects.filter(parent=obj1)
        for obj2 in taskObj:
            taskCount += 1
    return render(response, "content/overview.html", {"listCount":listCount, "taskCount":taskCount})

@login_required
def create(response):
    if response.method == "POST":
        user = response.user
        listName = response.POST.get('name')
        listObj = List.objects.create(user = user, name=listName)
        return redirect('add_and_edit', listId=listObj.id)
    return render(response, "content/create.html", {})

@login_required
def add_and_edit(response, listId):
    user = response.user
    if response.method == "POST":
        if response.POST.get('add') == 'add':
            newTask = response.POST.get('newTask')
            listObj = List.objects.get(user=user, id=listId)
            new_taskObj = Task.objects.create(parent=listObj, name=newTask, status=False)

        elif response.POST.get('save') == 'save':
            listObj = List.objects.get(user=user, id=listId)
            taskObj = Task.objects.filter(parent=listObj)
            for obj in taskObj:
                print(f'task{obj.id}')
                print(response.POST.get(f'task{obj.id}'))
                newStatus = response.POST.get(f'task{obj.id}')
                newDelete = response.POST.get(f'delete{obj.id}')
                if newStatus == 'yes':
                    obj.status = True
                    obj.save()
                else:
                    obj.status = False
                    obj.save()
                if newDelete == 'yes':
                    deletedTask = Task.objects.get(id=obj.id)
                    deletedTask.delete()
    
    tasks = []
    list = ''
    listObj = List.objects.get(user=user, id=listId)
    taskObj = Task.objects.filter(parent=listObj)
    for obj in taskObj:
        t_tuple = (obj.id, obj.name, obj.status)
        tasks.append(t_tuple)
    list = listObj.name
    print(tasks)
    return render(response, "content/add_and_edit.html", {"tasks":tasks, "list":list})

@login_required
def view(response):
    if response.method ==  "POST":
        user = response.user
        listObj = List.objects.filter(user=user)
        for obj1 in listObj:
            if response.POST.get(f'delete{obj1.id}') == 'delete':
                obj1.delete()
    data = []
    user = response.user
    listObj = List.objects.filter(user=user)
    for obj1 in listObj:
        total = completed = pending = 0
        taskObj = Task.objects.filter(parent=obj1)
        for obj2 in taskObj:
            total += 1
            if obj2.status == True:
                completed += 1
            else:
                pending += 1
        t_tuple = (obj1.id, obj1.name, total, completed, pending)
        data.append(t_tuple)
    return render(response, "content/view.html", {"data":data})