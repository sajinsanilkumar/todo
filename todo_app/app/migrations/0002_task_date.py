# Generated by Django 3.2.3 on 2021-05-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-03-18'),
            preserve_default=False,
        ),
    ]
