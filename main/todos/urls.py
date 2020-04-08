from django.urls import path
from .views import home,add_todo,delete_todo

app_name = 'todos'

urlpatterns = [
  path('',home,name='todos-list'),
  path('add/',add_todo,name='todos-add'),
  path('<int:id>/delete',delete_todo, name='todos-delete')
]