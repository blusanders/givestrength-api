# Generated by Django 3.2.4 on 2021-06-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givestrapi', '0012_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='gender',
            name='name',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
