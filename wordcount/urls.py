from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('word_insert', views.word_insert, name='word_insert'),
    path('counter', views.counter, name='counter')
]
