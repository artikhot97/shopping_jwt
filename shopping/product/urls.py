from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^users/register/$', RegisterView.as_view(), name='user-register'),
    url(r'register_manager/$', RegisterViewNormal.as_view(), name='register_manager'),
]