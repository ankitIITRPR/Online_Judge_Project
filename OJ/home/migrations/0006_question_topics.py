# Generated by Django 3.2.4 on 2021-07-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_submission_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.CharField(default='', max_length=100),
        ),
    ]
