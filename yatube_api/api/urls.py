from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'^posts/(?P<post_id>\d+)/comments/$', CommentViewSet, basename='CommentViewSet')
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
