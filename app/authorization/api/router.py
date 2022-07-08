from django.urls import path
from rest_framework import routers
from authorization.views import AuthView, RefreshView, RegistrationView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('login', AuthView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('register', RegistrationView.as_view()),
])