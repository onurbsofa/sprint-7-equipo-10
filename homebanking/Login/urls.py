from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Login import views

router = DefaultRouter()
router.register(r'Login', views.LoginAPIView)

urlpatterns = [
    path('', include(router.urls)),
]