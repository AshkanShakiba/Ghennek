from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import redirect

from .models import ShortenedURL


@api_view(["POST"])
def shortener(request):
    url = request.data["url"]
    obj = ShortenedURL.objects.create(url=url)
    return JsonResponse({"shorten_url": request.build_absolute_uri(f"/{obj.id}")})


@api_view(["GET"])
def redirector(request, pk):
    obj = ShortenedURL.objects.get(id=pk)
    return redirect(obj.url)
