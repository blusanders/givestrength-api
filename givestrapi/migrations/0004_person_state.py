# Generated by Django 3.2.4 on 2021-06-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givestrapi', '0003_auto_20210610_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(default='', max_length=2),
        ),
    ]
