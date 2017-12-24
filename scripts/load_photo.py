# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import tempfile

import requests
from django.core.files import File

from service.resource.models import Album


def get_cover(url):
    req = requests.get(url)
    tmp = tempfile.mktemp()

    print(url)
    print(tmp)

    if req.status_code == 200:

        open(tmp, 'wb').write(req.content)

        return File(open(tmp))
    else:
        return None


def run():
    Album.objects.all().delete()

    for x in open('init/items.jl'):
        x = json.loads(x)
        if x['data']['albums']:
            for album in x['data']['albums']:
                photos = []

                for p in album.get('photos'):
                    photos.append(p.get('url'))

                data = {
                    'title': album.get('content'),
                    'cover': album.get('girl').get('avatar'),
                    'status': 'published',
                    'picurl': photos,
                }

                try:
                    model, _ = Album.objects.get_or_create(**data)
                    model.save()
                    # model.cover.save('aaa.jpg', get_cover(album.get('girl').get('avatar')), save=True)
                except Exception as e:
                    raise e


if __name__ == '__main__':
    run()
