from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello I am there with u always")

def detail(request,question_id):
    return HttpResponse("You are looking at qustion %s" %question_id)
def results(request,question_id):
    response = "You are looking at qustion %s"
    return HttpResponse("response %question_id")
def vote(request,question_id):
    return HttpResponse("You are voting at question %s" %question_id)