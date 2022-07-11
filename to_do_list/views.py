from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_list.models import Tag, Task


def index(request):

    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request, 'to_do_list/index.html', context)


class TagsListView(generic.ListView):
    model = Tag


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('to_do_list:tag-list')


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('to_do_list:tag-list')


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'to_do_list/tag_confirm_delete.html'
    success_url = reverse_lazy('to_do_list:tag-list')


class TasksCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('to_do_list:index')
    queryset = Task.objects.all().select_related('tags')


class TasksUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('to_do_list:index')


class TasksDeleteView(generic.DeleteView):
    model = Task
    template_name = 'to_do_list/task_confirm_delete.html'
    success_url = reverse_lazy('to_do_list:index')


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.done = not task.done

    task.save()

    return HttpResponseRedirect(reverse_lazy("to_do_list:index"))
