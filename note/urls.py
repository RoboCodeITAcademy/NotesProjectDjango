from django.urls import path
from .import views

app_name = 'note'

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('create/', views.CreateNoteView.as_view(),name='create'),
	path('update/<pk>', views.UpdateNoteView.as_view(),name='update'),
	path('delete/<pk>', views.DeleteNoteView.as_view(), name='delete')

]