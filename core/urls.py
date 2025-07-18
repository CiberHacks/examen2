from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter
from core.views import ToDoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'api/todos', ToDoViewSet, basename='todo')

app_name = "core"

urlpatterns = [
    # CRUD Web
    path('todo/', views.ToDoList.as_view(), name="todo_list"),
    path('todo/create/', views.ToDoCreate.as_view(), name="todo_create"),
    path('todo/update/<int:pk>/', views.ToDoUpdate.as_view(), name="todo_update"),
    path('todo/delete/<int:pk>/', views.ToDoDelete.as_view(), name="todo_delete"),
    path('todo/detail/<int:pk>/', views.ToDoDetail.as_view(), name="todo_detail"),


    
    # Vista HTML desde API interna
    path('todos/internal/', views.ToDoInternalAPIList.as_view(), name='todo_internal_list'),

    # Endpoints JSON personalizados
    path('api/todos/ids/', views.ToDoIDsAPI.as_view(), name='api_todo_ids'),
    path('api/todos/id_title/', views.ToDoIDTitleAPI.as_view(), name='api_todo_id_title'),
    path('api/todos/pending/', views.ToDoPendingAPI.as_view(), name='api_todo_pending'),
    path('api/todos/done/', views.ToDoDoneAPI.as_view(), name='api_todo_done'),
    path('api/todos/id_user/', views.ToDoIDUserAPI.as_view(), name='api_todo_id_user'),
    path('api/todos/done_user/', views.ToDoDoneUserIDAPI.as_view(), name='api_todo_done_user'),
    path('api/todos/pending_user/', views.ToDoPendingUserIDAPI.as_view(), name='api_todo_pending_user'),
    path('core/', include(router.urls)),
]

# Incluye las rutas del ViewSet
urlpatterns += router.urls
