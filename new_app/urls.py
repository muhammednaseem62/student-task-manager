from django.urls import path
from .views import task_list, add_task,delete_task,complete_task,task_api

urlpatterns = [
    path('', task_list),
    path('add/', add_task),
    path('delete/<int:id>/', delete_task),
    path('complete/<int:id>/', complete_task),
    path('api/tasks/', task_api),
]