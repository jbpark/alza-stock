from django.conf.urls import url
from django.urls import path
from port import views

app_name = 'port'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.CreateView.as_view(), name='index'),
    path('', views.basic, name='index'),
    path('btest/<int:condition_id>/', views.btest, name='btest'),
    path('btest/<int:condition_id>/btest_graph/', views.btest_graph, name='btest_graph'),
    #path('btest/btest_graph/', views.btest_graph, name='btest_graph'),
    path('create', views.CreateView.as_view(), name='create'),
]