# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, AvatarViewSet, AddressViewSet, ContactViewSet, NoticesViewSet, ContainsViewSet, \
    FavoriteViewSet, FeedbackViewSet

router = DefaultRouter()
# router.register(r'address', AddressViewSet, 'me-address')
# router.register(r'contact', ContactViewSet, 'me-contact')
router.register(r'messages', NoticesViewSet, 'me-messages')
# router.register(r'contain', ContainsViewSet, 'me-contains')
router.register(r'favorite', FavoriteViewSet, 'me-favorite')
router.register(r'feedback', FeedbackViewSet, 'me-feedback')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^avatar/$', AvatarViewSet.as_view(), name='me-avatar'),
    url(r'^profile/$', ProfileViewSet.as_view(), name='me-profile'),
)
