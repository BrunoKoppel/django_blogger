# Generated by Django 3.2.8 on 2021-11-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfeed', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
