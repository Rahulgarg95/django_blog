from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author' : 'Rahul Garg',
        'title' : 'Blog Post 1',
        'content' : 'JNU protest issue rising every day',
        'date_posted' : 'Jan 11 2020'
    },
    {
        'author' : 'Rohit Agarwal',
        'title' : 'Blog Post 2',
        'content' : 'Amit Shah imposes CAA',
        'date_posted' : 'Jan 05 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About!!!'})