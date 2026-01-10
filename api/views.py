from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
    """Basic home endpoint."""
    return JsonResponse({
        'message': 'Welcome to Teacher Assistant API',
        'status': 'success'
    })


@require_http_methods(["GET"])
def health(request):
    """Health check endpoint."""
    return JsonResponse({
        'status': 'healthy',
        'service': 'teacher-assistant-backend'
    })
