from django.urls import path, include
from rest_framework import routers
from .views import UserCreateView, UserView, LoginView

router = routers.DefaultRouter()
router.register('users', UserView)

urlpatterns = [
  path('signup', UserCreateView.as_view()),
  path('login', LoginView.as_view()),
  path('', include(router.urls)),
]