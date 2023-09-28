# example/views.py
from datetime import datetime

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())