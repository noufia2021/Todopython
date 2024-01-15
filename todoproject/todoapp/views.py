from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    task_detials = Task.objects.all()
    if request.method=="POST":
        task=request.POST.get('task',)
        priority=request.POST.get('priority',)
        date= request.POST.get('date',)
        task1=Task(name=task,priority=priority,date=date)
        task1.save()
        return redirect('/')
    return render(request,"home.html",{'task_key':task_detials})

def delete(request,taskid):
    taskdel = Task.objects.get(id=taskid)
    if request.method=="POST":
        taskdel.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    todoupdata=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=todoupdata)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'todoupdata':todoupdata})

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_key'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

class Taskcreateview(CreateView):
    model = Task
    form_class = TodoForm
    template_name = 'create_view.html'
    success_url = reverse_lazy('cbvdetail')











