# Generated by Django 3.2 on 2021-05-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kofe',
            name='image',
            field=models.ImageField(blank=True, upload_to='coffee_images'),
        ),
    ]
