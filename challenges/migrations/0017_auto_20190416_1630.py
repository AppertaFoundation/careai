# Generated by Django 2.1.7 on 2019-04-16 16:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0016_auto_20190307_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='award',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='evaluation',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='rule',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='timeline',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
