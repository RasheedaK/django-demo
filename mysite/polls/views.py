from django.shortcuts import render
from django.forms import modelformset_factory

# Create your views here.
from django.http import HttpResponse
from .models import Login

def viewForm(request):
    loginFormSet = modelformset_factory(Login, fields=('username', 'password'), extra=1)
    if request.method == "POST":
        login=loginFormSet(request.POST, request.FILES)
        if login.is_valid():
            instance = login.save()[0]
            return render(request, 'welcome.html', {'user_name': instance.username})
        else:
            return HttpResponse("Invalid")
    return render(request, 'login.html', {'login_form': loginFormSet(queryset=Login.objects.none())})
# def aForm(request):

