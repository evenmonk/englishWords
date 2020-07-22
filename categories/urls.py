from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('categories/', views.CategoriesAPIView.as_view(), name='categories'),
    path('levels/', views.LevelsAPIView.as_view(), name='levels'),
    path('themes/', views.ThemesAPIView.as_view(), name='themes'),
    url(r'^themes/(?P<theme_id>[0-9]+)/$', views.ThemeAPIView.as_view(), name='theme'),
    url(r'^words/(?P<word_id>[0-9]+)/$', views.WordAPIView.as_view(), name='word')

]