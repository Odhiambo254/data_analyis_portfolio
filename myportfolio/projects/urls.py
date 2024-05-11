from django.urls import path
from pages import views as pages_views

urlpatterns=[
	path(''. pages_views.home,name='home'), #adding a home path 
	path('about/',pages_views.about, name='about')
]
