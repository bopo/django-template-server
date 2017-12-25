# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jsonfield
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel
from pilkit.processors import ResizeToFill

class Favorite(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _(u'收藏夹')
        verbose_name_plural = _(u'收藏夹')
        unique_together = ('owner', 'object_id', 'content_type')

class Profile(models.Model):
    '''
    该接口更新接受PUT方法
    性别字段英文对应汉字为:
    male:男
    female:女
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('', '未知'), ('male', '男'), ('female', '女'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True, related_name='profile')
    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=100, db_index=True)
    nick = models.CharField(verbose_name=_(u'昵称'), blank=True, null=True, max_length=100, db_index=True, default='')
    phone = models.CharField(verbose_name=_(u'银行预留电话'), default='', blank=True, max_length=64)
    gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
    idcard = models.CharField(verbose_name=_(u'身份证'), max_length=100, default='')
    birthday = models.DateField(_(u'生日'), blank=True, null=True)
    friend_verify = models.BooleanField(verbose_name=_(u'加好友时是否验证'), default=False)
    mobile_verify = models.BooleanField(verbose_name=_(u'是否允许手机号查找'), default=False)
    name_public = models.BooleanField(verbose_name=_(u'是否公开姓名'), default=False)
    avatar = ProcessedImageField(verbose_name=_(u'头像'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
        format='JPEG', null=True, default='avatar/default.jpg')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户信息')
        verbose_name_plural = _(u'用户信息')


class Address(TimeStampedModel):
    '''
    用户地址信息
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    name = models.CharField(verbose_name=_(u'联系人'), blank=True, null=True, max_length=100, db_index=True)
    mobile = models.CharField(verbose_name=_(u'手机号'), blank=True, null=True, max_length=100, db_index=True)
    area = models.CharField(verbose_name=_(u'市区'), blank=True, null=True, max_length=255, db_index=True)
    city = models.CharField(verbose_name=_(u'城市'), blank=True, max_length=255, db_index=True)
    address = models.CharField(verbose_name=_(u'详细地址'), blank=True, null=True, max_length=255, db_index=True)
    default = models.BooleanField(verbose_name=_('默认地址'), default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户地址')
        verbose_name_plural = _(u'用户地址')


class Contact(TimeStampedModel, StatusModel):
    '''
    用户通讯录
    '''
    STATUS = Choices(('invite', '邀请'), ('confirm', '确认'), ('new', '新用户'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('好友'), default='', related_name='friends')
    black = models.BooleanField(_('是否黑名单'), default=False)
    alias = models.CharField(_(u'备注别名'), max_length=100, default='')
    hide = models.BooleanField(_('别人不可见真名'), default=False)

    def __unicode__(self):
        return self.owner.username + '-' + self.friend.username

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户通讯录')
        verbose_name_plural = _(u'用户通讯录')
        unique_together = (("owner", "friend"),)


class Feedback(TimeStampedModel, StatusModel):
    '''
    用户反馈
    '''
    STATUS = Choices(('unread', '未读'), ('confirm', '确认'))

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    choices = models.CharField(verbose_name=_(u'反馈类型'), max_length=100, null=True)
    contact = models.CharField(verbose_name=_(u'联系方式'), max_length=200, default='')
    content = models.TextField(verbose_name=_(u'反馈内容'), null=True)

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'用户反馈')
        verbose_name_plural = _(u'用户反馈')


class Notice(TimeStampedModel):
    '''
    用户消息
    '''
    NOTICE_CHOICE = (('identity', '认证'), ('contract', '合约'), ('payment', '支付'), ('receive', '收货'), ('refunds', '退货'),)
    subject = models.CharField(verbose_name=_(u'消息主题'), max_length=255, default='')
    content = models.TextField(verbose_name=_(u'消息正文'), default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name=_(u'推送给用户'))
    extra = jsonfield.JSONField(verbose_name=u'附加内容', default={'data': "", 'type': ""})
    type = models.CharField(verbose_name=_(u'消息类型'), max_length=100, choices=NOTICE_CHOICE)

    def __unicode__(self):
        return '%s: %s' % (self.owner, self.subject)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        ordering = ('-pk',)
        verbose_name = _(u'消息中心')
        verbose_name_plural = _(u'消息中心')

# @receiver(signals.post_save, sender=Notice)
# def post_notice_push(instance, created, **kwargs):
#     if created:
#         return jpush_extras(message=str(instance.subject), alias=[instance.owner.mobile], extras=instance.extra)


# @receiver(signals.post_save, sender=Contact)
# def post_contact_push(instance, created, **kwargs):

#     if instance.status == 'invite':
#         return jpush_extras(message=str(instance.owner.profile.name + '请求添加您为好友'), alias=[instance.friend.mobile],
#                             extras={'type': instance.status, 'data': {
#                                 'friend_id': instance.friend.pk,
#                             }})
#     if not created:
#         if instance.status == 'confirm':
#             return jpush_extras(message=str(instance.owner.profile.name + '接受了您的添加请求'), alias=[instance.friend.mobile],
#                                 extras={'type': instance.status, 'data': {
#                                     'friend_id': instance.owner.pk,
#                                 }})
