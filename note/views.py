from django.shortcuts import render,redirect
from django.views.generic import View, ListView
from .models import Note
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)
from django.http import HttpResponse, JsonResponse
from .forms import AddNoteForm
# Create your views here.
class CreateNoteView(CreateView):
	model = Note
	fields = ['title','body','prioroty','star']
	success_url = '/'

class UpdateNoteView(UpdateView):
	model = Note
	fields = ['title', 'body', 'prioroty', 'star']
	success_url = '/'

class DeleteNoteView(DeleteView):
	model = Note
	success_url = '/'

class HomePageView(View):

	def get(self,request):
		notes = Note.objects.all()
		form = AddNoteForm()
		context = {
			'notes':notes,
			'form':form
		}
		return render(request, 'index.html', context)

	def post(self,request):
		form = AddNoteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('note:home')
		else:
			form = AddNoteForm()
		context = {
			'form':form
		}
		return render(request, 'index.html', context)

