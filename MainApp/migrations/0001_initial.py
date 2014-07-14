# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('solution', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('packing', models.CharField(max_length=1, choices=[(b'S', b'Strip'), (b'B', b'Bottle'), (b'P', b'Packet')])),
                ('mfg', models.DateField()),
                ('expiry', models.DateField()),
                ('saltinfo', models.TextField()),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('shipaddress', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(to='MainApp.Medicine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True)),
                ('userfname', models.CharField(max_length=50)),
                ('userlname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('useremail', models.EmailField(max_length=254)),
                ('userpass', models.CharField(max_length=20)),
                ('userph', models.IntegerField()),
                ('useradd1', models.CharField(max_length=70)),
                ('useradd2', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchase',
            name='userid',
            field=models.ForeignKey(to='MainApp.Users'),
            preserve_default=True,
        ),
    ]
