# Generated by Django 2.1.4 on 2019-04-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190320_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile-pics/default.jpg', upload_to='profile-pics'),
        ),
    ]
