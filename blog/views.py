from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        "author":"Anvesh Peddi",
        "title":"Post 1",
        "content":"This is first post!",
        "date_posted":"20th July, 2020"
    },
    {
        "author":"Damodar Peddi",
        "title":"Post 2",
        "content":"This is second post!",
        "date_posted":"21st July, 2020"
    }
]

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'posts':Post.objects.all()})

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
