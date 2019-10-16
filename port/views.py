from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
from port.btest import BackTest
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'port/index.html', context)

def btest(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    test = BackTest()
    test.run_test()
    return render(request, 'port/btest.html', context)

def btest_graph(request):
    my_file = open('D:\\jbdesk\\Dropbox\\jbmini\\project\\my\\stock\\alza-stock\\port\\templates\\port\\btest_graph.html','rb').read()
    return HttpResponse(my_file, content_type = 'text/html')