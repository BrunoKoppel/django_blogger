# Generated by Django 3.2.8 on 2021-11-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='The Blogger', max_length=255),
        ),
    ]
