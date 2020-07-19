from django.http import JsonResponse, HttpResponse
from categories.models import Category, Theme, Level, Word
from englishWords.settings import API_SECRET
from rest_framework.views import APIView
from categories.serializers import (CategoriesSerializer, WordSerializer, ThemesSerializer,
                                    LevelsSerializer, ThemeSerializer)
from django.shortcuts import render
from functools import wraps

def check_secret(method_to_decorate):
    """
    This decorator checks whether the secret in the request matches the secret in config.
    And if they doesn't match than return 403 error.
    :param method_to_decorate: method of the APIView class successor that we want to check.
    """
    @wraps(method_to_decorate)
    def wrapper(self, request, *args, **kwargs):
        if 'Secret' not in request.headers or request.headers['Secret'] == API_SECRET:
            return method_to_decorate(self, request, *args, **kwargs)
        return HttpResponse(status=403)
    return wrapper


class CategoriesAPIView(APIView):
    @check_secret
    def get(self, request, format=None):
        """
        Method, what returns response with all exist categories in our database.
        """
        serializer = CategoriesSerializer(Category.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class LevelsAPIView(APIView):
    @check_secret
    def get(self, request, format=None):
        """
        Method, what returns response with all exist levels in our database.
        """
        serializer = LevelsSerializer(Level.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class ThemesAPIView(APIView):
    @check_secret
    def get(self, request, format=None):
        """
        Method, what returns response with all exist themes in our database.
        """
        serializer = ThemesSerializer(Theme.objects.all(), many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class ThemeAPIView(APIView):
    @check_secret
    def get(self, request, theme_id, format=None):
        """
        Method, what returns response with theme by his primary key.
        """
        try:
            theme = Theme.objects.get(pk=theme_id)
        except Exception as e:
            return JsonResponse({'Error message': str(e)}, status=404)
        serializer = ThemeSerializer(theme)
        return JsonResponse(serializer.data, status=200)


class WordAPIView(APIView):
    @check_secret
    def get(self, request, word_id, format=None):
        """
        Method, what returns response with word by his primary key.
        """
        try:
            word = Word.objects.get(pk=word_id)
        except Exception as e:
            return JsonResponse({'Error message': str(e)}, status=404)
        serializer = WordSerializer(word)
        return JsonResponse(serializer.data, status=200)
