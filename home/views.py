from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy

from django.views import generic

from home.forms import LoginForm, UserForm
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
    
class Signup(generic.CreateView):
    template_name = 'home/signup.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('home:index')
        else:
            return redirect("home:index")
