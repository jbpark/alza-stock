from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question
from port.models import Condition
from port.btest import BackTest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from bootstrap_datepicker_plus import DateTimePickerInput
from django.shortcuts import resolve_url
from port.forms import BtestForm
import datetime
from django.shortcuts import redirect

app_name = 'port'
class CreateView(generic.edit.CreateView):
    model = Condition
    fields = ['code', 'start_date']

    #success_url = "/port/btest"

    def get_success_url(self):
        return resolve_url('/port/btest/' + str(self.object.id))

    def get_form(self):
        form = super().get_form()
        form.fields['start_date'].widget = DateTimePickerInput()
        return form

def _form_view(request, template_name='port/btest_form.html', form_class=BtestForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            stock_code = form.data['stock']
            start_date = datetime.datetime.strptime(form.data['start_date'], '%m/%d/%Y').strftime('%Y%m%d')
            end_date = datetime.datetime.strptime(form.data['end_date'], '%m/%d/%Y').strftime('%Y%m%d')
            #Condition.code = stock_code
            #Condition.start_date = start_date
            #Condition.end_date = end_date
            #Condition.save()
            condition = Condition()
            condition.code = stock_code
            condition.start_date = start_date
            condition.end_date = end_date
            condition.save()
            #return resolve_url('/port/btest/' + str(condition.pk))
            return redirect('/port/btest/' + str(condition.pk))
            #render(request, '/port/btest/' + str(condition.pk), {'form': form})

            #post.save()
            #return redirect('post_detail', pk=post.pk)
            #test = BackTest()
            #test.run_test(stock_code, start_date, end_date)
            #latest_question_list = Question.objects.all().order_by('-start_date')[:5]
            #context = {'latest_question_list': latest_question_list}
            #return render(request, 'port/btest.html', context)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def basic(request):
    return _form_view(request)

def index(request):
    latest_question_list = Question.objects.all().order_by('-start_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #form = super().get_form()
    #form.fields['start_date'].widget = DateTimePickerInput()
    return render(request, 'port/index.html', context)

def btest(request, condition_id):
    latest_question_list = Question.objects.all().order_by('-start_date')[:5]
    context = {'latest_question_list': latest_question_list}
    test = BackTest()
    condition = get_object_or_404(Condition, pk=condition_id)
    #stock_code = request.POST['stock_code']
    #start_date = request.POST['start_date']
    #end_date = request.POST['end_date']
    stock_code = condition.code
    start_date = condition.start_date
    end_date = condition.end_date
    #stock_code = condition.code;
    test.run_test(stock_code, start_date, end_date)
    return render(request, 'port/btest.html', context)

def btest_graph(request, condition_id):
#def btest_graph(request):
    my_file = open('D:\\jbdesk\\Dropbox\\jbmini\\project\\my\\stock\\alza-stock\\port\\templates\\port\\btest_graph.html','rb').read()
    return HttpResponse(my_file, content_type = 'text/html')