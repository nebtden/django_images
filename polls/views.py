from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.template import loader

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-id')
    # template = loader.get_template('polls/index.html')
    context = {
        "question_list":questions
    }
    return render(request,'polls/index.html',context)


def test(request):
    return HttpResponse("Hello, world. You're at the polls test.")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
