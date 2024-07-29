# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import RegisterViewSet, LoginView,employeeViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'employee',employeeViewSet,basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]