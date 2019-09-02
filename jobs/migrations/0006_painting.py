# Generated by Django 2.2.4 on 2019-09-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting_image', models.ImageField(upload_to='images/')),
                ('painting_title', models.CharField(default='SOME STRING', max_length=200)),
            ],
        ),
    ]