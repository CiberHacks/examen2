from django.shortcuts import render
from django.views import generic, View
from core import models, forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import JsonResponse

from .models import ToDo
from .serializers import (
    ToDoSerializer,
    ToDoIDSerializer,
    ToDoIDTitleSerializer,
    ToDoIDUserSerializer
)

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# ------------------ CRUD Web ------------------
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_status = self.request.query_params.get('status')
        user_id = self.request.query_params.get('user')

        if filter_status == 'completed':
            queryset = queryset.filter(is_completed=True)
        elif filter_status == 'pending':
            queryset = queryset.filter(is_completed=False)

        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        return queryset
    
class ToDoList(LoginRequiredMixin, generic.View):
    template_name = 'core/todo_list.html'
    login_url = "home:index"

    def get(self, request):
        todos = models.ToDo.objects.filter(user=request.user)
        return render(request, self.template_name, {'todos': todos})


class ToDoCreate(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/todo_create.html'
    model = models.ToDo
    form_class = forms.ToDoForm
    success_url = reverse_lazy("core:todo_internal_list")
    login_url = "home:index"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ToDoUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name = 'core/todo_update.html'
    model = models.ToDo
    form_class = forms.ToDoForm
    success_url = reverse_lazy("core:todo_internal_list")
    login_url = "home:index"


class ToDoDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'core/todo_delete.html'
    model = models.ToDo
    success_url = reverse_lazy("core:todo_internal_list")
    login_url = "home:index"


class ToDoDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'core/todo_detail.html'
    model = models.ToDo
    context_object_name = 'todo'
    login_url = "home:index"

# ------------------ API REST ------------------


class ToDoInternalAPIList(View):
    template_name = "core/todo_internal_list.html"

    def get(self, request):
        base_url = request.build_absolute_uri('/')[:-1]  # URL base sin slash final

        status = request.GET.get('filter')
        user_id = request.GET.get('user')

        # API por defecto
        api_url = f"{base_url}/core/api/todos/"

        # Cambiar URL según filtro
        if status == 'ids':
            api_url = f"{base_url}/core/api/todos/ids/"
        elif status == 'id_title':
            api_url = f"{base_url}/core/api/todos/id_title/"
        elif status == 'id_user':
            api_url = f"{base_url}/core/api/todos/id_user/"
        elif status == 'pending':
            api_url = f"{base_url}/core/api/todos/pending/"
        elif status == 'done':
            api_url = f"{base_url}/core/api/todos/done/"
        elif status == 'done_user':
            api_url = f"{base_url}/core/api/todos/done_user/"
        elif status == 'pending_user':
            api_url = f"{base_url}/core/api/todos/pending_user/"

        # Parámetros para enviar en la petición (en este caso solo el user_id si aplica)
        params = {}
        if user_id:
            params['user'] = user_id

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            todos = response.json()
            # Normalizar campo a booleano por si acaso
            for todo in todos:
                todo['is_completed'] = bool(todo.get('is_completed'))
        except requests.RequestException as e:
            print(f"Error al consumir API interna: {e}")
            todos = []

        context = {
            'todos': todos,
            'filter': status if status else 'all',
            'user_filter': user_id if user_id else '',
            'is_all_pending_done': status in (None, '', 'all', 'pending', 'done'),
            'is_ids': status == 'ids',
            'is_id_title': status == 'id_title',
            'is_id_user': status == 'id_user',
            'is_done_pending_user': status in ('done_user', 'pending_user'),
        }
        return render(request, self.template_name, context)






# ------------------ Endpoints JSON específicos ------------------

# Sólo IDs
class ToDoIDsAPI(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoIDSerializer

# IDs y Title
class ToDoIDTitleAPI(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoIDTitleSerializer

# Pendientes (no completados), ID y Title
class ToDoPendingAPI(generics.ListAPIView):
    serializer_class = ToDoIDTitleSerializer

    def get_queryset(self):
        return ToDo.objects.filter(is_completed=False)

# Resueltos (completados), ID y Title
class ToDoDoneAPI(generics.ListAPIView):
    serializer_class = ToDoIDTitleSerializer

    def get_queryset(self):
        return ToDo.objects.filter(is_completed=True)

# IDs y user_id
class ToDoIDUserAPI(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoIDUserSerializer

# Resueltos con user_id
class ToDoDoneUserIDAPI(generics.ListAPIView):
    serializer_class = ToDoIDUserSerializer

    def get_queryset(self):
        return ToDo.objects.filter(is_completed=True)

# Pendientes con user_id
class ToDoPendingUserIDAPI(generics.ListAPIView):
    serializer_class = ToDoIDUserSerializer

    def get_queryset(self):
        return ToDo.objects.filter(is_completed=False)