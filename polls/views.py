from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def meme(request):
    return HttpResponse("<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.latimes.com%2Fpolitics%2Fla-na-pol-pepe-the-frog-hate-symbol-20161011-snap-htmlstory.html&psig=AOvVaw0eCIYdXXcAReJk6Y5ka6NL&ust=1614509429344000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCKpbvyie8CFQAAAAAdAAAAABAD'>")