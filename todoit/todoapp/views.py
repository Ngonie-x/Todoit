from django.shortcuts import render, redirect
from .models import ToDo, Category
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    todos = ToDo.objects.all() #Querying all the todos with the object manager
    categories = Category.objects.all() # getting the categories with the object manager

    if request.method == 'POST':
        if "taskAdd" in request.POST:
            # checking if there is a request to add a todo
            user = request.user
            task_name = request.POST["description"] # task name
            date = str(request.POST["date"]) # date
            category = request.POST["category_select"]
            content = task_name + " -- " + date + " " + category

            Todo = ToDo(user=user, task_name=task_name, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
        
        if "taskDelete" in request.POST:
            # Delete a todo
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                print(todo_id)
                todo = ToDo.objects.get(id=int(todo_id))
                todo.delete()
    
    return render(request, "todoit/index.html", {"todos":todos, "categories":categories})
            


