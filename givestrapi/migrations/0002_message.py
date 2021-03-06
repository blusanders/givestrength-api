# Generated by Django 3.2.4 on 2021-06-10 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('givestrapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('maker', models.CharField(default='', max_length=55)),
                ('number_of_players', models.IntegerField(default=1)),
                ('skill_level', models.IntegerField(default=1)),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='givestrapi.person')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to='givestrapi.person')),
            ],
        ),
    ]
