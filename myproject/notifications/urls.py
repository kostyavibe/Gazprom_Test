from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
