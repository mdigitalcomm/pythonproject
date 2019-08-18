from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'first_tag': "This is my first tag!"}
    return render(request, 'appone/index.html', context=dict)