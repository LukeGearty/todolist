from django.urls import path
from . import views


urlpatterns = [
    path('',views.task_view, name='tasks'),
    path('completed/', views.completed, name='completed'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task')
]