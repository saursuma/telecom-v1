from django import forms
from models import Persons
from models import Comment

class PersonForm(forms.ModelForm):
	
	class Meta:
		model = Persons
		fields = ('first_name' , 'last_name','address', 'thumbnail')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('person', 'task', 'description', 'TaskType')

