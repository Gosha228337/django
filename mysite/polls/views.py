from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(reqeuest):
    latest_question_list = Question.objects.order_by("-pud_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "quest_list": latest_question_list,
    }
    return HttpResponse(template.render(context, reqeuest))


def detal(reqeuest, question_id):
    return HttpResponse("Ты ишешь вопрос номер %s" % question_id)

def results(reqeuest, question_id):
    return HttpResponse("Ты ишешь вопрос номер %s" % question_id)

def voite (reqeuest, question_id):
    return HttpResponse("Вы проголосовали за вопрос номер %s" % question_id)
