# Generated by Django 5.0.1 on 2024-01-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talaba',
            name='kitob_soni',
            field=models.IntegerField(default=1),
        ),
    ]
