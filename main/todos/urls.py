from django.urls import path
from .views import home,add_todo,delete_todo,edit_todo

app_name = 'todos'

urlpatterns = [
  path('',home,name='todos-list'),
  path('add/',add_todo,name='todos-add'),
  path('<int:id>/delete/',delete_todo, name='todos-delete'),
  path('<int:id>/edit/',edit_todo, name='todos-edit'),
]