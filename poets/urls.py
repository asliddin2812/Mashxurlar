from django.urls import path
from .views import poets_view, poets_detail_view

urlpatterns = [
    path('poet/<int:pk>/', poets_detail_view, name='poet_detail_view'),
    path('', poets_view, name='poets_view'),
]
