# Generated by Django 4.2.1 on 2023-05-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_allow',
            field=models.BooleanField(default=False),
        ),
    ]
