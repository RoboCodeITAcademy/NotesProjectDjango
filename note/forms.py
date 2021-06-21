from django import forms 
from .models import Note
from ckeditor.widgets import CKEditorWidget


class AddNoteForm(forms.ModelForm):
	body = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Note
		fields = '__all__'
		# exclude = ['body']
