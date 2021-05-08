from django import forms


class AddTodoForm(forms.Form):
    content = forms.CharField(label='TODO', max_length=159)
    deadline = forms.DateField(label='Deadline')
