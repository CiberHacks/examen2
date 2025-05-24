from django.shortcuts import render
from django.contrib.auth.models import User

from django.views import generic

# Create your views here.



class index(generic.View):
    template_name = 'home/index.html'
    context = {}

    def get(self, request):
        self.context = {
            "users": User.objects.all()
        }
        return render(request, self.template_name, self.context)

