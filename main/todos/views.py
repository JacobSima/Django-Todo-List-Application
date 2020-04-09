from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo


# Create your views here.
def mainHome(request):
  return render(request,'home.html',{})

def home(request):
  object_list = Todo.objects.all().order_by('-added_date')
  context = {
    'object_list':object_list
  }
  return render(request,'todos-home.html',context)



@csrf_exempt
def add_todo(request):
  date = timezone.now()
  added_date = date.strftime('%Y-%m-%d')
  text = request.POST.get('text')
  obj = Todo.objects.create(added_date=added_date,text=text)
  return redirect('/todos/1/')


def delete_todo(request,id):
  obj = Todo.objects.get(id = id)
  obj.delete()
  return redirect('/todos/1/')

@csrf_exempt
def edit_todo(request,id):
  obj = Todo.objects.get(id = id)
  if request.method == 'GET':
    context ={'obj':obj}
    return render(request,'todo-edit.html',context)
  elif request.method == 'POST':
    added_date = request.POST.get('date')
    text = request.POST.get('text')
    Todo.objects.filter(id = id).update(
      added_date = added_date,
      text = text
    )
  return redirect('/todos/1/')



