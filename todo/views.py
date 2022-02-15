from django.shortcuts import render, get_object_or_404
from todo.models import Todo 
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.

class ListTodoView(LoginRequiredMixin ,ListView):
    model = Todo
    template_name = 'todo/list.html'
    context_object_name = 'todos'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-time_created')



class CreateTodoView(LoginRequiredMixin, CreateView):
    model = Todo 
    fields = ['task']
    template_name = 'todo/create.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DetailTodoView(LoginRequiredMixin, DetailView):
    model = Todo 
    template_name = 'todo/detail.html'
    context_object_name = 'todos'




class UpdateTodoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo 
    template_name = 'todo/update.html'
    success_url = '/'
    fields = ['task']
    context_object_name = 'todos'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False




class DeleteTodoView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/'
    template_name = 'todo/delete.html'
    context_object_name = 'todos'


    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False



