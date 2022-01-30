from django import forms
from todo.models import Todo




class TodoForm(forms.ModelForm):

    class Meta:
        model =Todo 
        fields = ['todo_id',  'user','task']



        widgets ={
            'task': forms.TextInput(attrs:={'class':'taskInput', 'placeholder':'Task'})
        }




