import os
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.conf import settings

class FrontendAppView(View):
    def get(self, request, *args, **kwargs):
        try:
            with open(os.path.join(settings.BASE_DIR, 'frontend', 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "React build not found. Please build your React app first.",
                status=501,
            )

def login_view(request):
    return JsonResponse({"message": "login_view funcionando"})