# Generated by Django 2.1.5 on 2019-01-09 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_auto_20190109_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='users.Developer'),
        ),
    ]