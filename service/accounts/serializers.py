# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        # exclude = ('avatar',)


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='profile.name', label=u'姓名')
    nick = serializers.CharField(source='profile.nick', label=u'昵称')
    avatar = serializers.ImageField(source='profile.avatar', label=u'头像')

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'nick', 'avatar', 'mobile', 'level', 'avatar')


class NickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nick",)


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'city', 'area', 'address', 'name', 'mobile')
        # exclude = ('owner',)


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(source='friend.profile.name')
    nick = serializers.StringRelatedField(source='friend.profile.nick')
    level = serializers.StringRelatedField(source='friend.level')
    avatar = serializers.ImageField(source='friend.profile.avatar', read_only=True)
    userid = serializers.IntegerField(source='friend_id', read_only=True)

    class Meta:
        model = Contact
        fields = ('userid', 'nick', 'name', 'alias', 'black', 'avatar', 'hide', 'status', 'level')


class ContainsSerializer(serializers.ModelSerializer):
    contains = serializers.JSONField(label='通讯录数据')

    class Meta:
        model = Contains
        fields = ('contains',)


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('hide', 'black', 'alias')


class ContactHideSerializer(serializers.Serializer):
    userid = serializers.CharField(label='用户ID')

    class Meta:
        fields = ('userid',)


class ContactBlackSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(label='用户ID')

    class Meta:
        fields = ('userid',)


class AccountDetailsSerializer(serializers.ModelSerializer):
    avatar = serializers.ReadOnlyField(source='profile.avatar')
    birthday = serializers.ReadOnlyField(source='profile.birthday')
    nick = serializers.ReadOnlyField(source='profile.nick')
    name = serializers.ReadOnlyField(source='profile.name')
    gender = serializers.ReadOnlyField(source='profile.gender')

    class Meta:
        # depth = 1
        model = get_user_model()
        fields = ('url', 'nick', 'name', 'mobile', 'avatar', 'email', 'birthday', 'gender')

        # read_only_fields = ('email', 'username',)
        extra_kwargs = {
            # 'favorites': {'view_name': 'me-favorites-list', 'lookup_field': 'pk'},
            # 'profile': {'view_name': 'profile-detail', 'lookup_field': 'username', 'read_only': True, 'many': True},
        }


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        exclude = ('owner',)


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('friend_verify', 'mobile_verify', 'name_public')


class ContentTypeField(serializers.Field):
    def to_representation(self, obj):
        return obj.model

    def to_internal_value(self, data):
        return ContentType.objects.get(model=data)


# class ContentTypeField(serializers.Field):
#     def field_from_native(self, data, files, field_name, into):
#         into[field_name] = self.from_native(data[field_name])
#
#     def from_native(self, data):
#         app_label, model = data.split('.')
#         return ContentType.objects.get(app_label=app_label, model=model)
#
#     # If content_type is write_only, there is no need to have field_to_native here.
#     def field_to_native(self, obj, field_name):
#         if self.write_only:
#             return None
#         if obj is None:
#             return self.empty
#         ct = getattr(obj, field_name)
#         return '.'.join(ct.natural_key())


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('owner', 'modified', 'created', 'status_changed')


class FavoriteSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(source='object.title')
    type = serializers.StringRelatedField(source='content_type.model')

    class Meta:
        model = Favorite
        exclude = ('owner', 'modified', 'content_type')
        # fields = ('owner', 'content_type', 'object_id')
        # fields = '__all__'
        # depth = 1
