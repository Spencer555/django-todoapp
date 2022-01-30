from django.urls import path 
from todo.views import (
    ListTodoView,
    DeleteTodoView,
    CreateTodoView,
    UpdateTodoView,
    DetailTodoView
)



urlpatterns = [
    path('', ListTodoView.as_view(), name='list_todo'),


    path('create_todo/', CreateTodoView.as_view(), name='create_todo'),

    path('delete_todo/<slug:slug>/<int:pk>/', DeleteTodoView.as_view(), name='delete_todo'),

    path('detail_todo/<slug:slug>/<int:pk>/', DetailTodoView.as_view(), name='detail_todo'),


    path('update_todo/<slug:slug>/<int:pk>/', UpdateTodoView.as_view(), name='update_todo'),


]
