from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('list/banks/', views.ListBank.as_view(), name="list_bank"),
    path('detail/bank/<int:pk>', views.DetailBank.as_view(), name="detail_bank")

    
]