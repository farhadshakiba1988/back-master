from api.controllers.user_controller import *
from api.config import fake


class ComController:
    @staticmethod
    def fake_chart_data(request):
        return JsonResponse(fake.data())

    @staticmethod
    def auth_routes(request):
        return JsonResponse(fake.auth_routes())

    @staticmethod
    def project_notice(request):
        return JsonResponse(fake.notice())

    @staticmethod
    def activities(request):
        return JsonResponse(fake.activities(), safe=False)

    @staticmethod
    def forms(request):
        return JsonResponse(fake.forms())

    @staticmethod
    def fake_list(request):
        return JsonResponse(fake.fake_list(), safe=False)

    @staticmethod
    def profile_basic(request):
        return JsonResponse(fake.profile_basic(), safe=False)

    @staticmethod
    def profile_advanced(request):
        return JsonResponse(fake.profile_advanced(), safe=False)

    @staticmethod
    def notices(request):
        return JsonResponse(fake.notices(), safe=False)
