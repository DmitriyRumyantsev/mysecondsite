from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"
    def get_queryset(self):
        return Question.objects.all()

def meme(request):
    return HttpResponse("<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.latimes.com%2Fpolitics%2Fla-na-pol-pepe-the-frog-hate-symbol-20161011-snap-htmlstory.html&psig=AOvVaw0eCIYdXXcAReJk6Y5ka6NL&ust=1614509429344000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCKpbvyie8CFQAAAAAdAAAAABAD'>")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def vote(request, q_id):

    question = Question.objects.get(pk=q_id)
    choices = request.POST.getlist("choice")
 
    for elem in choices:
        choice = question.choice_set.get(pk=elem)
        choice.votes +=1
        choice.save()
    return HttpResponseRedirect(reverse("polls:result", args=(q_id, )))

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"    