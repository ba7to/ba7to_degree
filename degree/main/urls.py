from django.urls import path
from . import views
urlpatterns = [
    path('',views.message),
    path('dd/',views.Dd),
]