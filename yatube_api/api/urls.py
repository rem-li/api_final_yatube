from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FoolowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'groups', GroupViewSet, basename='groups')
router.register('follow', FoolowViewSet, basename='follow')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
