# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygon', '0009_auto_20180702_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_code', models.TextField()),
                ('grader_code', models.TextField()),
                ('language', models.CharField(choices=[('c', 'C'), ('cpp', 'C++11'), ('python', 'Python 3'), ('java', 'Java 8'), ('cc14', 'C++14'), ('cs', 'C#'), ('py2', 'Python 2'), ('php', 'PHP 7'), ('perl', 'Perl'), ('hs', 'Haskell'), ('js', 'Javascript'), ('ocaml', 'OCaml'), ('pypy', 'PyPy'), ('pas', 'Pascal'), ('rs', 'Rust'), ('scala', 'Scala')], default='cpp', max_length=12)),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='revision',
            name='templates',
            field=models.ManyToManyField(to='polygon.Template'),
        ),
    ]
