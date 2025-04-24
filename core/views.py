from django.shortcuts import render
from django.http import JsonResponse
import json

from django.conf import settings
import os

print("📂 staticfiles dir:", settings.STATIC_ROOT)
print("📂 Contenido:", os.listdir(settings.STATIC_ROOT))

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')

def experiencias(request):
    return render(request, 'core/experiencias.html')

def webhook_n8n(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Datos recibidos desde n8n:", data)
        return JsonResponse({"status": "ok", "received": data})
    return JsonResponse({"error": "Método no permitido"}, status=405)
