from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Menu

# Create your views here.
def index(request):
     menu = Menu.objects.order_by('-id')
     template = loader.get_template('menu.html')
     context = {
        'latest_menu': menu,
    }
     return HttpResponse(template.render(context, request))