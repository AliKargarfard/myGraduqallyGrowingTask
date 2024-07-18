from django.urls import path
from .views import ListTask, CreateTask, CompleteTask, UnCompleteTask, UpdateTask, DeleteTaskView

urlpatterns = [
    path('', ListTask.as_view(), name='list_tasks'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('complete/<int:pk>/', CompleteTask.as_view(), name='task_done'),
    path('uncomplete/<int:pk>/', UnCompleteTask.as_view(), name='task_undone')
]