from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('login')
        messages.error(request, form.errors)
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))