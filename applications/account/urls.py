from django.urls import path

from applications.account.views import RegisterAPIView, ActivationAPIView, ChangePasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>', ActivationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordAPIView.as_view()),


]
