from django.http import JsonResponse
from api.models.user import User
from django.forms.models import model_to_dict


class UserController:

    @staticmethod
    def index(request):
        return JsonResponse(model_to_dict(User.objects.first()), safe=False)
