from django.http import JsonResponse
from .models import *
from django.forms.models import model_to_dict


def index(request):
    return JsonResponse(model_to_dict(User.objects.first()), safe=False)


def auth_routes(request):
    fake_data = {"/form/advanced-form": {"authority": ["admin", "user"]}}
    return JsonResponse(fake_data)


def rule(request):
    return JsonResponse(request.GET)
