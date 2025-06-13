from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views import generic

from home.forms import LoginForm
# Create your views here.



class index(generic.View):
    template_name = 'home/index.html'
    context = {}
    form_class = LoginForm

    def get(self, request):
        self.context = {
            "users": User.objects.all(),
            "loginForm": self.form_class
        }
        return render(request, self.template_name, self.context)
    

    def post(self, request ):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return redirect('home:index')


class Logout(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        logout(request)
        return redirect("home:index")