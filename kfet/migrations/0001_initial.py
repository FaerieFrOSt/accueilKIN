# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=5, decimal_places=2, blank=True)),
                ('number_of_products', models.SmallIntegerField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('gadz', models.ForeignKey(related_name='user_gadz', to='users.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('reference', models.CharField(max_length=8)),
                ('category', models.ForeignKey(to='kfet.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='kfet.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(related_name='user_vendor', to='users.Client'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='entity',
            field=models.ForeignKey(to='kfet.Entity'),
            preserve_default=True,
        ),
    ]
