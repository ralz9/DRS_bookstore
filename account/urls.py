from django.urls import path

from account.views import RegisterAPIView, ActivationAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>', ActivationAPIView.as_view()),
]
