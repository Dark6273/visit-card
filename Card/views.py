from django.db.models import IntegerField
from django.db.models import Value, F, ExpressionWrapper
from django.db.models.functions import Concat
from django.shortcuts import render
from django.utils import timezone

from .models import PersonalInfo


def index(request):
    personal_info = PersonalInfo.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name'),
        age=ExpressionWrapper(timezone.now() - F('birth_date'), output_field=IntegerField())
    ).first()

    return render(request, 'index.html', {'personal_info': personal_info})
