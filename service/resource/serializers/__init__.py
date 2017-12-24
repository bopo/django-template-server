# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from taggit.models import Tag

from service.resource.models.resource import Banner
from ..models import Catalog, Album, Video, Author, Article, Comment, Counties
from ..models import Version


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('version', 'depends', 'install', 'sha1sum', 'channel', 'constraint', 'summary')


class CountiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counties
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'name',)


class AlbumSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()

    class Meta:
        model = Album
        exclude = ('status', 'status_changed', 'checker_runtime', 'source_site', 'picurl', 'owner', 'url')


class AlbumDetailSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()

    class Meta:
        model = Album
        exclude = ('status', 'status_changed', 'checker_runtime', 'source_site', 'url')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()

    class Meta:
        model = Video
        exclude = ('status', 'status_changed', 'checker_runtime', 'video_website', 'owner', 'url')


class VideoDetailSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = Video
        exclude = ('status', 'status_changed', 'owner', 'url')


class ArticleSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()

    class Meta:
        model = Article
        exclude = ('status', 'status_changed', 'content', 'owner')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    category = CatalogSerializer()

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('status', 'status_changed', 'owner')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
