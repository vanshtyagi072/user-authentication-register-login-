from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api_app.models import Register
from api_app.serializers import RegisterSerializer
from django.shortcuts import render

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True}, status=201)
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    elif request.method == 'GET':
        return render(request, 'register.html')  # Make sure 'register.html' exists in your templates directory
    else:
        return JsonResponse({'message': 'Method not allowed.'}, status=405)




