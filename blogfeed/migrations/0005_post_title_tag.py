# Generated by Django 3.2.8 on 2021-11-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogfeed', '0004_remove_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='the blogger', max_length=255),
        ),
    ]