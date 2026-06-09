from django.shortcuts import render

from django.http import JsonResponse

def get_users(request):
    return JsonResponse({"message": "ok"})