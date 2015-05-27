# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='name', db_index=True)),
                ('display_name', models.CharField(max_length=200, verbose_name='display name', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('klass', models.CharField(help_text=b'Example: notifier.backends.EmailBackend', max_length=500, verbose_name='class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPrefs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('notify', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(to='notifier.Backend')),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Group prefs',
                'verbose_name_plural': 'Group prefs',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='name', db_index=True)),
                ('display_name', models.CharField(max_length=200, verbose_name='display name')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('backends', models.ManyToManyField(to='notifier.Backend', verbose_name='backends', blank=True)),
                ('permissions', models.ManyToManyField(to='auth.Permission', verbose_name='permissions', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SentNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('success', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('backend', models.ForeignKey(to='notifier.Backend')),
                ('notification', models.ForeignKey(to='notifier.Notification')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPrefs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('notify', models.BooleanField(default=True)),
                ('backend', models.ForeignKey(to='notifier.Backend')),
                ('notification', models.ForeignKey(to='notifier.Notification')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User prefs',
                'verbose_name_plural': 'User prefs',
            },
        ),
        migrations.AddField(
            model_name='groupprefs',
            name='notification',
            field=models.ForeignKey(to='notifier.Notification'),
        ),
        migrations.AlterUniqueTogether(
            name='userprefs',
            unique_together=set([('user', 'notification', 'backend')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupprefs',
            unique_together=set([('group', 'notification', 'backend')]),
        ),
    ]
