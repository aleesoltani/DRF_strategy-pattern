from django.urls import path
from .views import TestCreateAPIView, TestRetrieveAPIView, UserRetrieveAPIView

urlpatterns = [
    path('create', TestCreateAPIView.as_view()),
    path('get/<int:pk>', UserRetrieveAPIView.as_view()),
    path('test/<int:pk>', TestRetrieveAPIView.as_view())
]