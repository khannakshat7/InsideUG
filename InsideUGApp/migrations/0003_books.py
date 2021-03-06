# Generated by Django 3.0.7 on 2020-07-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsideUGApp', '0002_course_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('stream', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('link', models.URLField()),
                ('smallImage', models.FileField(upload_to='booksmall/')),
                ('BigImage', models.FileField(upload_to='bookbig/')),
            ],
        ),
    ]
