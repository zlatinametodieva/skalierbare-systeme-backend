from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Todo
from .forms import AddTodoForm


def index_view(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': zip(range(1, len(todo_list) + 1), todo_list)}

    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = Todo(content=form.cleaned_data['content'], deadline=form.cleaned_data['deadline'])
            todo.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html', context)


def impressum_view(request):
    return render(request, 'impressum.html')
