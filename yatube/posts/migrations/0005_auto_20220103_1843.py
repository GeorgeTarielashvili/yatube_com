# Generated by Django 2.2.19 on 2022-01-03 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220103_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='group',
        ),
    ]
