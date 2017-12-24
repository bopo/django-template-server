# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from service.resource.models import Counties
import json


def save(pid=0):
	try:
		data = open('scripts/data/%s.txt.json' % pid).read()
		data = json.loads(data)
	except Exception as e:
		return

	for x in data:
		print(x)
		pid = None if pid==0 else pid
		obj, _ = Counties.objects.get_or_create(name = x['label'], id = x['value'], parent_id=pid)
		obj.save()

		save(pid=x['value'])

def run():
	Counties.objects.all().delete()
	save()