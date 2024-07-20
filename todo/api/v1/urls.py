"""# from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('task',views.TaskModelViewSet,basename='task')
# router.register('category',views.CategoryModelViewSet,basename='category')
urlpatterns = router.urls
"""

from django.urls import path, include
from .views import taskList, taskDetail

app_name = 'api-v1'

urlpatterns = [
    path('task/', taskList, name='task_list'),
    path('task/<int:id>/', taskDetail, name='task_detail'),
]