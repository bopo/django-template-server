# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status, filters
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from taggit.models import Tag

from service.resource.models.resource import Banner
from ..models import Album, Catalog, Video, Author, Article, Favorite, Comment, Counties
from ..models import Version
from ..serializers import AlbumSerializer, CatalogSerializer, VideoSerializer, AuthorSerializer, ArticleSerializer, \
    ArticleDetailSerializer, VideoDetailSerializer, AlbumDetailSerializer, LikeSerializer, TagsSerializer, \
    CommentSerializer, CountiesSerializer, BannerSerializer
from ..serializers import VersionSerializer


class VersionViewSet(viewsets.GenericViewSet):
    '''
    用户信息
    '''
    serializer_class = VersionSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        return Version.objects.order_by('-id').first()


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(status='published')
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = ArticleDetailSerializer
        return super(ArticleViewSet, self).retrieve(request, *args, **kwargs)

    @detail_route(methods=['GET'], permission_classes=(IsAuthenticated,))
    def favorite(self, request, pk=None):
        instance = self.get_object()

        try:
            event = Favorite(owner=request.user, object=instance)
            event.save()

            instance.favCount += 1
            instance.save()

            return Response({'detail': '收藏成功'})
        except Exception as e:
            return Response({'detail': '重复收藏'}, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['GET'], permission_classes=(IsAuthenticated,))
    def like(self, request, pk=None, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'detail': '成功'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['GET', 'POST'])
    def comment(self, request, pk=None, *args, **kwargs):
        if request.method == 'POST':
            return Response({'detail': 'POST'})
        else:
            self.serializer_class = CommentSerializer
            queryset = Comment.objects.all()

            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class AlbumViewSet(ArticleViewSet):
    queryset = Album.objects.filter(status='published')
    serializer_class = AlbumSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = AlbumDetailSerializer
        return super(AlbumViewSet, self).retrieve(request, *args, **kwargs)


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class VideoViewSet(ArticleViewSet):
    queryset = Video.objects.filter(status='published')
    serializer_class = VideoSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = VideoDetailSerializer
        return super(VideoViewSet, self).retrieve(request, *args, **kwargs)


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CountiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Counties.objects.all()
    serializer_class = CountiesSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('id',)
    search_fields = ('^name',)
    filter_fields = '__all__'
