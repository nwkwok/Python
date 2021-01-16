from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Nick Kwok',
        'title': 'Blog Post #1',
        'content': 'This is my first post',
        'date_posted': 'January 15th, 2021'
    },
    {
        'author': 'Natalia Kwok',
        'title': 'Blog Post #2',
        'content': 'This is the second post on the blog',
        'date_posted': 'January 16th, 2021'
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "Django Blog - About"})
