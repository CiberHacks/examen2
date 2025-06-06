from django.shortcuts import render
from django.views import generic
from core import models
from django.urls import reverse_lazy

from core import forms
# Create your views here.

class ListBank(generic.View):
    template_name = 'core/list_bank.html'
    context = {}


    def get(self, request):
            self.context = {
                'banks': models.Bank.objects.filter(status=True)
            }
            return render(request, self.template_name, self.context)
    

class DetailBank(generic.View):
    template_name = 'core/detail_bank.html'
    context = {}


    def get(self, request, pk):
            self.context = {
                'banks': models.Bank.objects.get(pk=pk)
            }
            return render(request, self.template_name, self.context)
    
class CreateBank(generic.CreateView):
    template_name = "core/create_bank.html"
    model = models.Bank
    form_class = forms.CreateBankForm
    success_url = reverse_lazy("core:list_bank")


class UpdateBank(generic.UpdateView):
    template_name = "core/update_bank.html"
    model = models.Bank
    form_class = forms.UpdateBankForm
    success_url = reverse_lazy("core:list_bank")

class DeleteBank(generic.DeleteView):
    template_name = "core/delete_bank.html"
    model = models.Bank
    success_url = reverse_lazy("core:list_bank")