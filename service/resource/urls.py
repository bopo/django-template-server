# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'counties', CountiesViewSet, base_name='counties')
router.register(r'version', VersionViewSet, base_name='version')
router.register(r'catalog', CatalogViewSet, base_name='catalog')
router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'banner', BannerViewSet, base_name='banner')
router.register(r'comment', CommentViewSet, base_name='comment')
# router.register(r'author', AuthorViewSet, base_name='author')
# router.register(r'albums', AlbumViewSet, base_name='albums')
# router.register(r'videos', VideoViewSet, base_name='videos')
# router.register(r'tags', TagsViewSet, base_name='tags')

urlpatterns = (
    url(r'^', include(router.urls, namespace='v1.0')),
    url(r'^me/', include('service.customer.urls')),
    url(r'^auth/', include('service.passport.urls')),
    url(r'^user/', include('rest_framework.urls', namespace='rest_framework')),
)
