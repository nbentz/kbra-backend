# Generated by Django 4.0.6 on 2022-07-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
    ]