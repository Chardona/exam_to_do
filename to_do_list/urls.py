from django.urls import path

from to_do_list.views import (
    index,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    TasksCreateView,
    TasksUpdateView,
    TasksDeleteView,
    change_task_status
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/create', TasksCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TasksUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TasksDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/', change_task_status, name='task-change-status'),
    path('tags/', TagsListView.as_view(), name='tag-list'),
    path('tags/create', TagsCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update', TagsUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete', TagsDeleteView.as_view(), name='tag-delete'),

]

app_name = 'to_do_list'
