# Generated by Django 2.1.3 on 2018-11-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0006_auto_20180809_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatelog',
            name='log_type',
            field=models.CharField(choices=[('fix', '问题修复'), ('add', '新功能'), ('del', '删除功能'), ('ref', '重构'), ('upd', '更新'), ('enhance', '加强')], max_length=10),
        ),
    ]