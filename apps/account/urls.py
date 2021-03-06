# coding:utf8
from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 使用自动URL路由连接我们的API。
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
