# Generated by Django 2.2.3 on 2019-07-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]