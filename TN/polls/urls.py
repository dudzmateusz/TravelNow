from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('schedule/', views.ScheduleCreateView.as_view(), name='schedule'),
    path('schedule/found/', views.ScheduleCreateView.login, name='schedule_found'),
    path('schedule/found/hotels/', views.ScheduleCreateView.testa, name='hotels'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]