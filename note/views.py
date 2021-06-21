from django.shortcuts import render,redirect
from django.views.generic import View, ListView
from .models import Note

from django.http import HttpResponse
from .forms import AddNoteForm
# Create your views here.


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

import json
def starUnstar(request):
	d = request.GET['data']
	print(d)
	data = json.loads(d)
	return HttpResponse('is worked ')