# Generated by Django 2.2.4 on 2019-09-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_painting'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='edu_period',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='period',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
