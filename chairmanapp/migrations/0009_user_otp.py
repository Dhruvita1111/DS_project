# Generated by Django 4.1.7 on 2023-03-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0008_alter_societymember_contact_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=456),
        ),
    ]
