from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
# from django.core import serializers

from .models import Badge

def list(request):
    qs = Badge.objects.values('id','name','desc')

    data = []
    for b in qs:
        data.append(b)

    return JsonResponse({'badges' : data })

def list_user_badges(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    qs = user.badge_set.values('id','name','desc')

    badges = []
    for b in qs:
        badges.append(b)

    data = {
        'id': user.id,
        'username': user.username,
        'badges': badges,
    }

    return JsonResponse(data)
