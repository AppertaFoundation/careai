# Generated by Django 2.1.4 on 2018-12-23 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('data', models.FileField(upload_to='')),
                ('clinician', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='users.Clinician')),
                ('developers', models.ManyToManyField(to='users.Developer')),
            ],
        ),
    ]