from rest_framework import serializers
from categories.models import Category, Word, Theme, Level


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ['theme']


class ThemeSerializer(serializers.ModelSerializer):
    words = serializers.SerializerMethodField(method_name='get_words')

    def get_words(self, instance):
        return WordSerializer(instance.word_set.all(), many=True).data

    class Meta:
        model = Theme
        fields = '__all__'