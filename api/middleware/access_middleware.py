from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


class AccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        try:
            if not request.user.has_access:
                raise PermissionDenied
        except:
            return HttpResponse('401 Unauthorized', status=401)
