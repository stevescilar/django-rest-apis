from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi steve this is your django api response"})
