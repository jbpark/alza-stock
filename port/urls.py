from django.conf.urls import url
from django.urls import path
from port import views

app_name = 'port'
urlpatterns = [
    path('', views.index, name='index'),  # /port/
    path('btest/', views.btest, name='btest'),
    path('btest/btest_graph/', views.btest_graph, name='btest_graph'),
]