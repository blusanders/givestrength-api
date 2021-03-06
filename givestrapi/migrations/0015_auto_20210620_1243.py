# Generated by Django 3.2.4 on 2021-06-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givestrapi', '0014_auto_20210615_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='popup',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='street',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='zip',
            field=models.CharField(default='', max_length=5),
        ),
    ]
