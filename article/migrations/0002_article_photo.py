# Generated by Django 4.1 on 2022-08-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
