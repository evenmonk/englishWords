from django.contrib import admin
from categories.models import Category, Level, Word, Theme


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    readonly_fields = ['audio_tag']

admin.site.register(Level)
