from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Todo
from .forms import AddTodoForm, EditTodoForm, DeleteTodoForm


def index_view(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': zip(range(1, len(todo_list) + 1), todo_list)}

    if request.method == 'POST':
        add_todo_form = AddTodoForm(request.POST)
        edit_todo_form = EditTodoForm(request.POST)
        delete_todo_form = DeleteTodoForm(request.POST)

        if add_todo_form.is_valid():
            todo = Todo(content=add_todo_form.cleaned_data['content'], deadline=add_todo_form.cleaned_data['deadline'])
            todo.save()
        if edit_todo_form.is_valid():
            Todo.objects.filter(id=edit_todo_form.cleaned_data['n']).update(content=edit_todo_form.cleaned_data['cont'],
                                                                            deadline = edit_todo_form.cleaned_data['dline'],
                                                                            progress = edit_todo_form.cleaned_data['prog'])
        if delete_todo_form.is_valid():
            Todo.objects.filter(id=delete_todo_form.cleaned_data['id']).delete()
        return HttpResponseRedirect('/')

    else:
        return render(request, 'index.html', context)


def impressum_view(request):
    return render(request, 'impressum.html')