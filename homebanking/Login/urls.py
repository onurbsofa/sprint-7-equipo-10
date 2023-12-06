from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Login import views
from Login.views import RegisterAPIView

router = DefaultRouter()
router.register(r'Login', views.LoginAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register')
]