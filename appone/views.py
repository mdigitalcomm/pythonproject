from django.shortcuts import render
from appone.models import Website, Topic
from appone.forms import MyModelform

# Create your views here.


def index(request):
    websites_list = Website.objects.all()
    dict = {'websites_list': websites_list}
    return render(request, 'appone/index.html', context=dict)


def myform(request):
    if request.method == 'POST':
        form = MyModelform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        form = MyModelform()
    return render(request, 'appone/myform.html', {'form': form})
