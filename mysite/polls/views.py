from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse,Http404
"""from django.template import loader"""

from .models import Question

# Create your views here.
"""def index1(request):
    return HttpResponse("Hello I am there with u always")
def index2(request):
    latest_question_list = Question.objects.order_by("-pub_date[:5]")
    output = " , ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list":latest_question_list,
    }
    return HttpResponse(template.render(context,request))
"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)

"""def detail1(request,question_id):
    return HttpResponse("You are looking at qustion %s" %question_id)"""
"""def detail2(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,"polls/detail.html",{"question":question})"""

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    response = "You are looking at qustion %s"
    return HttpResponse("response %question_id")
def vote(request,question_id):
    return HttpResponse("You are voting at question %s" %question_id)