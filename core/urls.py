from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('list/banks/', views.ListBank.as_view(), name="list_bank"),
    path('create/banks/', views.CreateBank.as_view(), name="create_bank"),
    path('detail/bank/<int:pk>', views.DetailBank.as_view(), name="detail_bank"),
    path('update/bank/<int:pk>', views.UpdateBank.as_view(), name="update_bank"),
    path('delete/bank/<int:pk>', views.DeleteBank.as_view(), name="delete_bank")

]