# Generated by Django 3.2.4 on 2021-06-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givestrapi', '0005_auto_20210611_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(max_length=255),
        ),
    ]
