# Generated by Django 4.2.5 on 2023-09-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movies_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='sddd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]