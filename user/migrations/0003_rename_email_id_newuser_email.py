# Generated by Django 5.0.6 on 2024-07-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_email_newuser_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='email_id',
            new_name='email',
        ),
    ]
