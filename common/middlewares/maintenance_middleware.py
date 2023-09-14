from django.conf import settings
from django.http import JsonResponse
from rest_framework.status import HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.response import Response


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.MAINTENANCE_MODE:
            return JsonResponse({"error": "Service under maintenance!"}, status=503)
        return self.get_response(request)
