from django.forms import Form, CharField, IntegerField, ChoiceField, DateField, TextInput, Select, ModelForm
from .models import Todo


class TodoForm(Form):
    title = CharField(widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(widget=TextInput(attrs={"class": "form-control"}))
    progress = IntegerField()
    status = ChoiceField(choices=Todo.TASK_STATUSES, widget=Select)


class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'progress', 'status'] # __all__
        # exclude = []