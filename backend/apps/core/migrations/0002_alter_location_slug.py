# Generated by Django 3.2 on 2022-05-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, max_length=8, null=True),
        ),
    ]
