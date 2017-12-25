# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from service.accounts.models import Contact, Notice, Profile, Contains, Feedback
from service.resource.models import Favorite
from .serializers import AddressSerializer, AvatarSerializer, \
    ContactDetailSerializer, ContactHideSerializer, ContactSerializer, ContainsSerializer, NoticeSerializer, \
    ProfileSerializer, FavoriteSerializer, FeedbackSerializer
from .utils import get_user_profile


class ProfileViewSet(RetrieveUpdateAPIView):
    '''
    用户信息
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()

    def get_object(self):
        return get_user_profile(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class AvatarViewSet(ProfileViewSet):
    '''
    头像上传接口.

    '''
    serializer_class = AvatarSerializer


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.address_set.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save()


class ContactViewSet(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    '''
    联系人接口
    --------

    - 上传通讯录 POST /api/me/contact/contains/
    - 设置黑名单 POST /api/me/contact/{pk}/
    - 批量隐藏我名字(批量) POST /api/me/contact/black/
    - 批量隐藏我名字 POST /api/me/contact/hide/
    - 批量黑名单 POST /api/me/contact/black/

    `hide 和 black 接口 psot 参数 userid 为多个 id 用 "," 隔开`

    status 三种状态: new 手机通讯录用户 invite 邀请用户 confirm 确认状态


    '''
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    lookup_field = 'friend_id'

    def get_queryset(self):

        # queryset = self.queryset.filter(
        #     Q(owner=self.request.user, status='confirm') | Q(owner=self.request.user, status='new') | Q(
        #         friend=self.request.user, status='invite')).exclude(
        #     black=True)

        queryset = self.queryset.filter(owner=self.request.user).exclude(black=True)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ContactDetailSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @list_route(methods=['GET', 'POST'])
    def hide(self, request, *args, **kwargs):
        self.serializer_class = ContactHideSerializer
        if request.method == 'POST':
            userid = request.data['userid'].replace(u'，', '.')
            Contact.objects.filter(friend__in=userid.split(','), owner=request.user).update(hide=True)
            return Response({'detail': '成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': '不支持 GET 方法'}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['GET', 'POST'])
    def black(self, request, *args, **kwargs):
        self.serializer_class = ContactHideSerializer
        if request.method == 'POST':
            userid = request.data['userid'].replace(u'，', '.')
            Contact.objects.filter(friend__in=userid.split(','), owner=request.user).update(black=True)
            return Response({'detail': '成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': '不支持 GET 方法'}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['GET', 'POST'])
    def contains(self, request, *args, **kwargs):
        '''
        [
            {
                "name": "BellKate",
                "phoneNum": [
                    "(555) 564-8583",
                    "(415) 555-3695"
                ]
            },
            {
                "name": "BellKate",
                "phoneNum": [
                    "(555) 564-8583",
                    "(415) 555-3695"
                ]
            },
        ]

        '''
        self.serializer_class = ContainsSerializer
        # # 解析数据
        contains = request.data.get('contains')

        try:
            contains = json.loads(contains)
        except Exception:
            return Response({'detail': 'JSON格式错误'}, status=status.HTTP_400_BAD_REQUEST)

        # 取出所有手机号
        mobiles = []
        contact = {}

        for contain in contains:
            if contain.get('phoneNum'):
                for phone in contain.get('phoneNum'):
                    mobiles.append(phone)
                    contact[phone] = contain.get('name')

        mobiles = list(set(mobiles))

        # 读取数据库里的含税含有手机号列表的数据
        detail = '通讯录没有变化'

        try:
            users = get_user_model().objects.filter(mobile__in=mobiles)

            for user in users:
                obj, st = Contact.objects.get_or_create(owner=self.request.user, friend=user)

                if st:
                    obj.alias = contact[user.mobile]
                    obj.status = 'new'
                    obj.save()

            detail = '通讯录更新成功'
        except User.DoesNotExist:
            pass

        return Response({'detail': detail}, status=status.HTTP_200_OK)


class ContainsViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ContainsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contains.objects.all()
    lookup_field = 'mobile'

    def create(self, request, *args, **kwargs):
        contains = request.data.get('contains')
        querysetlist = []

        for kwargs in contains:
            querysetlist.append(Contains(kwargs))

        Contains.objects.bulk_create(querysetlist)
        return Response('JSON格式错误', status=status.HTTP_201_CREATED)


class NoticesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Notice.objects.filter(owner=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('content_type', 'content_type__model')

    def get_queryset(self):
        queryset = Favorite.objects.filter(owner=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset


class FeedbackViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
