# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals, absolute_import

# from django.conf import settings
# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.contrib.contenttypes.models import ContentType
# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _
# # from dynamic_scraper.models import Scraper, SchedulerRuntime
# # from jsonfield import JSONField
# from model_utils import Choices
# from model_utils.models import StatusModel
# from model_utils.models import TimeStampedModel
# from mptt.fields import TreeForeignKey
# from mptt.models import MPTTModel
# # from scrapy_djangoitem import DjangoItem
# # from taggit.managers import TaggableManager

# CHANNEL_CHOICES = Choices(
#     ('ios', _('IOS')),
#     ('android', _('Android')),
# )

# PLATFORM_CHOICES = Choices(
#     ('ios', _('IOS')),
#     ('android', _('Android')),
# )

# UNITS_CHOICES = Choices(
#     ('ios', _('IOS')),
#     ('android', _('Android')),
# )


# # Favorite


# # @python_2_unicode_compatible
# # class Author(TimeStampedModel):
# #     name = models.CharField(verbose_name=_(u'模特名称'), max_length=64, null=False)
# #     cover = models.ImageField(verbose_name=_(u'模特图片'), max_length=200, blank=True, null=True, upload_to='author')
# #     total = models.IntegerField(verbose_name=_(u'模特数'), blank=True, null=True, default=0)
# #     order = models.PositiveIntegerField(verbose_name=_(u'排序'), default=999, editable=False)

# #     def __str__(self):
# #         return self.__unicode__()

# #     class Meta:
# #         verbose_name = _(u'模特列表')
# #         verbose_name_plural = _(u'模特列表')


# @python_2_unicode_compatible
# class Catalog(MPTTModel):
#     name = models.CharField(verbose_name=_(u'分类名称'), max_length=64, null=False)
#     cover = models.ImageField(verbose_name=_(u'分类图片'), max_length=200, blank=True, null=True, upload_to='catalog')
#     total = models.IntegerField(verbose_name=_(u'图片数'), blank=True, null=True, default=0)
#     order = models.PositiveIntegerField(verbose_name=_(u'排序'), default=999, editable=False)
#     parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
#     url = models.URLField(verbose_name='链接', blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _(u'类别列表')
#         verbose_name_plural = _(u'类别列表')

#     class MPTTMeta:
#         order_insertion_by = ['order']
#         parent_attr = 'parent'


# @python_2_unicode_compatible
# class SourceSite(models.Model):
#     name = models.CharField(verbose_name='站点名称', max_length=200)
#     url = models.URLField(verbose_name='网址 URL')

#     # scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='采集器')
#     # scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL,
#     #     verbose_name='采集运行器')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _(u'采集源站')
#         verbose_name_plural = _(u'采集源站')


# @python_2_unicode_compatible
# class Album(TimeStampedModel, StatusModel):
#     STATUS = Choices(('draft', '草稿'), ('published', '发布'))

#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'所有者'), default=0)
#     title = models.CharField(verbose_name=_(u'名称'), max_length=100, default='')
#     summary = models.TextField(verbose_name=_(u'描述'), default='')
#     type = models.CharField(verbose_name=_(u'类型'), max_length=50, choices=UNITS_CHOICES)
#     cover = models.URLField(verbose_name=_(u'封面'), null=True, help_text=u'图片尺寸最好为720x240')
#     likeCount = models.IntegerField(verbose_name='喜欢数', default='0')
#     # picurl = JSONField(verbose_name='图片链接', blank=True, null=True)
#     favCount = models.IntegerField(_(u'收藏数'), default='0')
#     category = models.ForeignKey(Catalog, verbose_name='类别', default=0)
#     comment = GenericRelation('Comment')

#     # tags = TaggableManager()

#     # url = models.URLField(blank=True, default='')
#     # source_site = models.ForeignKey(SourceSite, default=0)
#     # checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = _(u'相册列表')
#         verbose_name_plural = _(u'相册模块')


# @python_2_unicode_compatible
# class Video(TimeStampedModel, StatusModel):
#     STATUS = Choices(('draft', '草稿'), ('published', '发布'))

#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'所有者'))
#     title = models.CharField(verbose_name=_(u'视频名称'), max_length=100, default='')
#     summary = models.TextField(verbose_name=_(u'视频描述'), default='')
#     type = models.CharField(verbose_name=_(u'视频类型'), max_length=50, choices=UNITS_CHOICES)
#     favCount = models.IntegerField(_(u'收藏数'), default='0')
#     # cover = ProcessedImageField(verbose_name=_(u'封面'), upload_to='sounds', processors=[ResizeToFill(720, 240)],
#     # format='JPEG', null=True, help_text=u'图片尺寸最好为720x240')
#     cover = models.URLField(verbose_name=_(u'封面'), null=True, help_text=u'图片尺寸最好为720x240')
#     mp4url = JSONField(verbose_name='播放列表', blank=True, null=True)
#     likeCount = models.IntegerField(verbose_name='喜欢数', default='0')
#     category = models.ForeignKey(Catalog, verbose_name='类别')
#     comment = GenericRelation('Comment')

#     # tags = TaggableManager()

#     # url = models.URLField(blank=True, default='')
#     # video_website = models.ForeignKey(SourceSite)
#     # checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = _(u'视频列表')
#         verbose_name_plural = _(u'视频模块')


# @python_2_unicode_compatible
# class Article(TimeStampedModel, StatusModel):
#     STATUS = Choices(('draft', '草稿'), ('published', '发布'))

#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'所有者'), blank=True, null=True)
#     title = models.CharField(verbose_name=_(u'标题'), max_length=100, default='')

#     summary = models.TextField(verbose_name=_(u'描述'), blank=True, null=True)
#     content = models.TextField(verbose_name=_(u'正文'), blank=True, null=True)

#     favCount = models.IntegerField(_(u'收藏数'), default='0')
#     category = models.ForeignKey(Catalog, verbose_name='类别', blank=True, null=True)
#     likeCount = models.IntegerField(verbose_name='喜欢数', default='0')

#     image_list = JSONField(verbose_name='图片列表', blank=True)
#     video_list = JSONField(verbose_name='视频列表', blank=True)
#     display_url = models.URLField(verbose_name='展示url', blank=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = _(u'图文列表')
#         verbose_name_plural = _(u'图文模块')


# class Comment(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL)
#     body = models.TextField(blank=True)
#     # content_type = models.ForeignKey(ContentType)
#     # object_id = models.PositiveIntegerField()
#     # content_object = GenericForeignKey()
#     content_id = models.ForeignKey(Article, blank=True, default=None)

#     class Meta:
#         verbose_name = _(u'评论列表')
#         verbose_name_plural = _(u'评论模块')


# class Banner(models.Model):
#     # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
#     title = models.CharField(max_length=100, blank=True)
#     picurl = models.URLField(blank=True)

#     class Meta:
#         verbose_name = _(u'广告列表')
#         verbose_name_plural = _(u'广告模块')


# # class VideoItem(DjangoItem):
# #     django_model = Video


# # class ArticleItem(DjangoItem):
# #     django_model = Article


# # class AlbumItem(DjangoItem):
# #     django_model = Album

# class Counties(MPTTModel):
#     name = models.CharField(verbose_name=_(u'区县名称'), max_length=64, null=False)
#     order = models.PositiveIntegerField(verbose_name=_(u'排序'), default=999, editable=False)
#     parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _(u'区县列表')
#         verbose_name_plural = _(u'区县列表')

#     class MPTTMeta:
#         order_insertion_by = ['order']
#         parent_attr = 'parent'


# class Favorite(TimeStampedModel):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL)

#     content_type = models.ForeignKey(ContentType, blank=True, null=True)
#     object_id = models.PositiveIntegerField(blank=True, null=True)
#     object = GenericForeignKey('content_type', 'object_id')

#     class Meta:
#         verbose_name = _(u'收藏夹')
#         verbose_name_plural = _(u'收藏夹')
#         unique_together = ('owner', 'object_id', 'content_type')


# class Version(TimeStampedModel):
#     version = models.CharField(verbose_name=_(u'版本号'), max_length=10, null=False, default='1.0.0')
#     depends = models.CharField(verbose_name=_(u'依赖版本'), max_length=10, null=True, blank=True)
#     install = models.FileField(upload_to='versions', verbose_name=_(u'下载链接'), name='install', null=True)
#     sha1sum = models.CharField(verbose_name=_(u'校验码'), max_length=64, null=True, blank=True)
#     channel = models.CharField(verbose_name=_(u'渠道'), max_length=10, blank=False, choices=CHANNEL_CHOICES)
#     summary = models.TextField(verbose_name=_(u'日志'), default='')
#     platform = models.CharField(verbose_name=_(u'APP平台'), max_length=50, default='android', choices=PLATFORM_CHOICES)
#     constraint = models.BooleanField(verbose_name=_(u'强更'), default=False)

#     def __unicode__(self):
#         return self.version

#     def __str__(self):
#         return self.version

#     def save(self, *args, **kwargs):
#         import hashlib
#         sha1 = hashlib.sha1()

#         for chunk in self.install.chunks():
#             sha1.update(chunk)

#         self.sha1sum = sha1.hexdigest()
#         self.install.name = '%s.apk' % self.sha1sum
#         super(Version, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name = _(u'版本升级')
#         verbose_name_plural = _(u'版本升级')
#         unique_together = ('version', 'channel',)
