from django.http import JsonResponse, HttpResponse
from .models import Category, Theme, Level, Word
from englishWords.settings import API_SECRET
from rest_framework.views import APIView
from categories.serializers import (CategoriesSerializer, WordSerializer, ThemesSerializer,
                                    LevelsSerializer, ThemeSerializer)
from django.shortcuts import render
from functools import wraps
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LevelsSerializer


def check_secret(method_to_decorate):
    # checking for a match of secrets
    @wraps(method_to_decorate)
    def wrapper(self, request, *args, **kwargs):
        if 'Secret' not in request.headers or request.headers['Secret'] == API_SECRET:
            return method_to_decorate(self, request, *args, **kwargs)
        # returns 403 error if they don't match
        return HttpResponse(status=403)
    return wrapper


class CategoriesAPIView(APIView):
    # returns all categories in db
    @check_secret
    def get(self, request, format=None):
        serializer = CategoriesSerializer(Category.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class LevelsAPIView(APIView):
    # returns all levels in db
    @check_secret
    def get(self, request, format=None):
        serializer = LevelsSerializer(Level.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class ThemesAPIView(APIView):
    # returns all themes in db
    @check_secret
    def get(self, request, format=None):
        serializer = ThemesSerializer(Theme.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class ThemeAPIView(APIView):
    # returns response with theme by his primary key.
    @check_secret
    def get(self, request, theme_id, format=None):
        try:
            theme = Theme.objects.get(pk=theme_id)
        except Exception as e:
            return JsonResponse({'Error message': str(e)}, status=404)
        serializer = ThemeSerializer(theme)
        return JsonResponse(serializer.data, status=200)


class WordAPIView(APIView):
    # returns response with word by his primary key.
    @check_secret
    def get(self, request, word_id, format=None):
        try:
            word = Word.objects.get(pk=word_id)
        except Exception as e:
            return JsonResponse({'Error message': str(e)}, status=404)
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data, status=200)


@api_view(['GET', 'POST'])
def get_post_levels(request):
    # get all levels
    if request.method == 'GET':
        return Response({})
    # insert a new record for a level
    elif request.method == 'POST':
        return Response({})
