# Generated by Django 3.1 on 2020-09-06 22:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20200907_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Подробное описание'),
        ),
    ]
