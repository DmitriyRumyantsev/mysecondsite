from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.


def index(request):
    question = Question.objects.all()

    context = {
        "questions" : question
    }
    return render(request, "polls/index.html", context)

def meme(request):
    return HttpResponse("<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.latimes.com%2Fpolitics%2Fla-na-pol-pepe-the-frog-hate-symbol-20161011-snap-htmlstory.html&psig=AOvVaw0eCIYdXXcAReJk6Y5ka6NL&ust=1614509429344000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCKpbvyie8CFQAAAAAdAAAAABAD'>")

def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }
    return render(request, "polls/detail.html", context)

def results(request, q_id):
    res = "Result question № %s." % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question № %s." % q_id
    return HttpResponse(res)