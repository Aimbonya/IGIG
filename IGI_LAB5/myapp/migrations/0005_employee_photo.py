# Generated by Django 5.0.6 on 2024-05-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='photo_2022-12-25_17-03-47.jpg', upload_to='posters/'),
        ),
    ]
