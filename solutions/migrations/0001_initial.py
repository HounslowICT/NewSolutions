# Generated by Django 5.1.5 on 2025-01-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('solution', models.TextField(max_length=1500)),
                ('clase', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=500)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
