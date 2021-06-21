from django.urls import path
from .import views

app_name = 'note'

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('stars/', views.starUnstar, name='starUnstar'),
]