from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''Welcome to my word counter project'''
def home(request):
    response = render(request, 'home.html')
    return response

'''Here is where the user inserts the words'''
def word_insert(request):
    response = render(request, 'submit.html')
    return response

'''This is the results page'''
def counter(request):
    text = request.POST['text']
    num_of_words = len(text.split())
    response = render(request, 'display.html', {'passed_words': num_of_words})
    return response