from django.urls import path
from . import views

urlpatterns = [
    path('articles',views.homepage1)
]
