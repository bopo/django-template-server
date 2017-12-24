# -*- coding: utf-8 -*-
from django.contrib import admin

from service.resource.models.resource import Banner
from ..models import Author, Catalog, SourceSite, Album, Video, Article, Comment, Favorite


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'name',
        'cover',
        'total',
        'order',
    )
    list_filter = ('created', 'modified')
    search_fields = ('name',)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'cover',
        'total',
        'order',
        'parent',
        'lft',
        'rght',
        'tree_id',
        'level',
    )
    list_filter = ('parent',)
    search_fields = ('name',)


@admin.register(SourceSite)
class SourceSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    search_fields = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'status',
        'status_changed',
        'owner',
        'title',
        'summary',
        'type',
        'cover',
        'likeCount',
        'picurl',
        'favCount',
        'category',
    )
    list_filter = (
        'created',
        'modified',
        'status_changed',
        'owner',
        'category',
    )
    raw_id_fields = ('tags',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'status',
        'status_changed',
        'owner',
        'title',
        'summary',
        'type',
        'favCount',
        'cover',
        'mp4url',
        'likeCount',
        'category',
    )
    list_filter = (
        'created',
        'modified',
        'status_changed',
        'owner',
        'category',
    )
    raw_id_fields = ('tags',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'picurl')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created',
        'modified',
    )
    list_filter = (
        'created',
        'modified',
        'status',
        'category',
    )
    # raw_id_fields = ('tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'body', 'content_id')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'owner',
        'content_type',
        'object_id',
    )
    list_filter = ('created', 'modified', 'owner', 'content_type')
