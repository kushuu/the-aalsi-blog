from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('competitive_programming', views.cp, name = "cp"),
    path('cyber_security', views.cyber, name = "cyber"),
    path('machine_learning', views.ml, name = "ml"),
    path('trivia', views.trivia, name = "trivia"),
    path('articles', views.all_articles, name = "all"),
    path('contact', views.contact, name = "contact"),
    path('article/<str:title>', views.article, name = "article"),
    path('update_like', views.update_like, name = "update_like"),
]