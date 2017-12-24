# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import tempfile
# from cStringIO import StringIO
# from random import choice

import qrcode
# import short_url
# from PIL import Image
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render
# from service.customer.models import Profile
# from .models import QRToken
# from .utiils import logo_abb, merge_image


# def generate_qrcode(data, size=11):
#     qr = qrcode.QRCode(version=1, box_size=size, border=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
#     qr.add_data(data)
#     qr.make(fit=True)
#     im = qr.make_image()

#     return im


# def qs(request, key):
#     # 生成扫码登陆图片

#     try:
#         token = QRToken.objects.filter(key=key).get()
#         img = generate_qrcode(token.raw)
#         buf = StringIO()
#         img.save(buf)

#         stream = buf.getvalue()
#         return HttpResponse(stream, content_type="image/jpeg")
#     except QRToken.DoesNotExist:
#         # 不存在提示
#         return HttpResponse('key 参数错误')


# def scan_login(request):
#     # 生成token
#     token = QRToken()

#     # 生成url
#     done = 'http://' + request.get_host() + '/api/qrlogin/%s/done/' % token.key
#     scan = 'http://' + request.get_host() + '/api/qrlogin/%s/scan/' % token.key
#     cancel = 'http://' + request.get_host() + '/api/qrlogin/%s/cancel/' % token.key
#     check = 'http://' + request.get_host() + '/api/qrlogin/%s/check/' % token.key

#     # 写入数据库
#     token.raw = {'type': 'qrlogin', 'data': json.dumps({'done': done, 'scan': scan, 'cancel': cancel}).encode('hex')}
#     token.save()

#     key = token.key

#     return render(request, 'scanlogin.html', locals())


# def video(request):

#     return render(request, 'video.html')


def video_iframe(request):
    return render(request, 'video_iframe.html', locals())
