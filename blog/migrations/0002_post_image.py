# Generated by Django 2.0.4 on 2018-05-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=12, upload_to='post_images'),
            preserve_default=False,
        ),
    ]
