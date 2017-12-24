# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 23:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import jsonfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='联系人')),
                ('mobile', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='手机号')),
                ('area', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='市区')),
                ('city', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='城市')),
                ('address', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='详细地址')),
                ('default', models.BooleanField(default=False, verbose_name='默认地址')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户地址',
                'verbose_name_plural': '用户地址',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('invite', '邀请'), ('confirm', '确认'), ('new', '新用户')], default='invite', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('black', models.BooleanField(default=False, verbose_name='是否黑名单')),
                ('alias', models.CharField(default='', max_length=100, verbose_name='备注别名')),
                ('hide', models.BooleanField(default=False, verbose_name='别人不可见真名')),
                ('friend', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='好友')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户通讯录',
                'verbose_name_plural': '用户通讯录',
            },
        ),
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('mobile', models.CharField(default='', max_length=100, verbose_name='手机号码')),
                ('alias', models.CharField(default='', max_length=100, verbose_name='备注别名')),
            ],
            options={
                'verbose_name': '手机通讯录',
                'verbose_name_plural': '手机通讯录',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('unread', '未读'), ('confirm', '确认')], default='unread', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('choices', models.CharField(max_length=100, null=True, verbose_name='反馈类型')),
                ('contact', models.CharField(default='', max_length=200, verbose_name='联系方式')),
                ('content', models.TextField(null=True, verbose_name='反馈内容')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户反馈',
                'verbose_name_plural': '用户反馈',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('subject', models.CharField(default='', max_length=255, verbose_name='消息主题')),
                ('content', models.TextField(default='', verbose_name='消息正文')),
                ('extra', jsonfield.fields.JSONField(default={'data': '', 'type': ''}, verbose_name='附加内容')),
                ('type', models.CharField(choices=[('identity', '认证'), ('contract', '合约'), ('payment', '支付'), ('receive', '收货'), ('refunds', '退货')], max_length=100, verbose_name='消息类型')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='推送给用户')),
            ],
            options={
                'verbose_name': '消息中心',
                'verbose_name_plural': '消息中心',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='姓名')),
                ('nick', models.CharField(blank=True, db_index=True, default='', max_length=100, null=True, verbose_name='昵称')),
                ('phone', models.CharField(blank=True, default='', max_length=64, verbose_name='银行预留电话')),
                ('gender', models.CharField(choices=[('', '未知'), ('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('idcard', models.CharField(default='', max_length=100, verbose_name='身份证')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('friend_verify', models.BooleanField(default=False, verbose_name='加好友时是否验证')),
                ('mobile_verify', models.BooleanField(default=False, verbose_name='是否允许手机号查找')),
                ('name_public', models.BooleanField(default=False, verbose_name='是否公开姓名')),
                ('avatar', imagekit.models.fields.ProcessedImageField(default='avatar/default.jpg', null=True, upload_to='avatar', verbose_name='头像')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([('owner', 'friend')]),
        ),
    ]
