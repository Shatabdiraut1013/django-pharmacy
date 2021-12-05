from django.shortcuts import render
from .models import Blogpost, Popularpost
# Create your views here.
def index(request):
    mypost = Blogpost.objects.all()
    poppost = Popularpost.objects.all()
    return render(request, 'blog/index.html',{'mypost':mypost, 'poppost':poppost})

def popularpost(request,id):
    popularpost = Popularpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/popularpost.html',{'popularpost':popularpost})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',{'post':post})