from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
@login_required
def index(request):
    my_models = MyModel.objects.all()
    return render(request, 'web/index.html', {'my_models': my_models})
