from django.shortcuts import render
from django.views import generic
from core import models

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