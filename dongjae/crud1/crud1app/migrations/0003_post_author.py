# Generated by Django 4.2.1 on 2023-05-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1app', '0002_post_comment_allow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
