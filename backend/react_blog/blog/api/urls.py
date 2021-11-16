from django.urls import path

from blog.api import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
]