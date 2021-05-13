from django import forms


class AddTodoForm(forms.Form):
    content = forms.CharField(label='TODO', max_length=159)
    deadline = forms.DateField(label='Deadline')


class DeleteTodoForm(forms.Form):
    id = forms.IntegerField(label='id')


class EditTodoForm(forms.Form):
    n = forms.IntegerField(label='id')
    cont = forms.CharField(label='TODO', max_length=159)
    dline = forms.DateField(label='Deadline')
    prog = forms.IntegerField(label='Progress')
