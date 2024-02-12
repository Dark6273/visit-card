from django.shortcuts import render
from .models import PersonalInfo


def index(request):
    personal_info = PersonalInfo.objects.first()
    return render(request, 'index.html', {'personal_info': personal_info})
