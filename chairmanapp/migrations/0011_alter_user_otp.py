# Generated by Django 4.1.7 on 2023-03-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0010_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=456),
        ),
    ]
