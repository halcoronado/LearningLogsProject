from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(requests):
    topics = Topic.objects.all()

    context = {'topics': topics}

    return render(requests, 'MainApp/topics.html', context)

