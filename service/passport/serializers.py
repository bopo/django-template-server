# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from .forms import SetPasswordForm


class VerifySerializer(serializers.Serializer):
    username = serializers.CharField(label=_(u'手机号码'), required=True, allow_blank=False)

    def validate_username(self, value):
        """
        判断手机是否匹配规格
        """
        rule = r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'

        if not re.match(rule, value):
            raise serializers.ValidationError(_("手机号码格式不匹配."))

        return value


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(label=_(u'手机号'), required=True, allow_blank=False)
    password = serializers.CharField(label=_(u'新密码'), required=True, style={'input_type': 'password'})
    verify = serializers.CharField(label=_(u'验证码'), required=True, allow_blank=False)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, label=u'手机号码')
    password = serializers.CharField(required=True, style={'input_type': 'password'}, label=u'登录密码')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # 判断手机是否匹配规格
        rule = r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        if not re.match(rule, username):
            raise ValidationError(_("手机号码格式不匹配."))

        if username and password:
            user = authenticate(username=username, password=password)
        else:
            raise ValidationError(_('必须包含手机号和密码.'))

        if user:
            if not user.is_active:
                raise ValidationError(_('用户帐户被禁用.'))
        else:
            raise ValidationError(_('手机号或密码错误,无法登录.'))

        attrs['user'] = user
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = Token
        fields = ('key',)


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = get_user_model()
        # fields = ('username', 'email', 'first_name', 'last_name')
        # read_only_fields = ('email',)


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    username = serializers.CharField(label='手机号码')

    def validate_username(self, value):
        # 判断手机是否匹配规格
        UserModel = get_user_model()

        rule = r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        if not re.match(rule, value):
            raise ValidationError(_("手机号码格式不匹配."))

        try:
            user = UserModel.objects.filter(username=value)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError('手机号码不存在')

        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    username = serializers.CharField(required=True, label='手机号')
    password = serializers.CharField(style={'input_type': 'password'}, required=True, max_length=128, label='新密码')
    verify = serializers.CharField(required=True, label='验证码')

    set_password_form_class = SetPasswordForm

    def validate(self, attrs):
        UserModel = get_user_model()
        self._errors = {}

        try:
            self.user = UserModel._default_manager.get(username=attrs['username'])
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        self.set_password_form.save()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'}, max_length=128, label='旧密码')
    new_password1 = serializers.CharField(style={'input_type': 'password'}, max_length=128, label='新密码')
    new_password2 = serializers.CharField(style={'input_type': 'password'}, max_length=128, label='确认密码')

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(settings, 'OLD_PASSWORD_FIELD_ENABLED', False)
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')

        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(user=self.user, data=attrs)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        self.set_password_form.save()
