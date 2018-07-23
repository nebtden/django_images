from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    data = ','.join([q.question_text for q in questions])
    return HttpResponse(data)


def test(request):
    return HttpResponse("Hello, world. You're at the polls test.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
