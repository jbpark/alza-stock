from django.conf.urls import url
from django.urls import path
from polls import views
from django.http import HttpResponse
import datetime

# returns current time in html
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),  # /polls/
    path('<int:question_id>/', views.detail, name='detail'),  # /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),  # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),  # /polls/5/vote/
    url(r'^time/$', current_datetime), # http://localhost:8080/polls/time/
]