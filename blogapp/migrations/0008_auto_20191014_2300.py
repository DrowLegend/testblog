# Generated by Django 2.2.5 on 2019-10-14 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20191014_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='name',
        ),
    ]
