from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
router.register(r'giftboxes', GiftBoxViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
