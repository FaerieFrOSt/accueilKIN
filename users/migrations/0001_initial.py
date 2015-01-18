# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bucque', models.CharField(max_length=255, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'/static/avatar/', blank=True)),
                ('signature', models.TextField(blank=True)),
                ('credit', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('famss', models.CharField(max_length=255, verbose_name="Fam'ss", blank=True)),
                ('promss', models.IntegerField(null=True, verbose_name="prom'ss", blank=True)),
                ('kgibss', models.CharField(max_length=4, verbose_name='Chambre')),
                ('phone', models.CharField(max_length=10, verbose_name='T\xe9l\xe9phone')),
                ('date_negatss', models.DateTimeField(null=True, blank=True)),
                ('has_rezal', models.BooleanField(default=False)),
                ('is_gadz', models.BooleanField(default=False)),
                ('is_debucquable', models.BooleanField(default=False)),
                ('radcheck_password', models.CharField(max_length=253)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='radcheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(max_length=64)),
                ('op', models.CharField(default=b'==', max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radcheck',
            },
            bases=(models.Model,),
        ),
    ]
