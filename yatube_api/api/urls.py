from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()

router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)

router.register('api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')


from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [

    path('api/v1/api-token-auth/', rest_framework_views.obtain_auth_token),
    path('', include(router.urls)),
]