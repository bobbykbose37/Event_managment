# Generated by Django 3.2 on 2021-04-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
    ]
