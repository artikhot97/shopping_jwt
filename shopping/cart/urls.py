from django.conf.urls import url, include
from rest_framework import routers
from api.views import CartViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]