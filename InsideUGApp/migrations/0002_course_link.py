# Generated by Django 3.0.7 on 2020-07-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsideUGApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(default='http://google.com'),
            preserve_default=False,
        ),
    ]