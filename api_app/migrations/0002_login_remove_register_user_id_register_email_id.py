# Generated by Django 5.0.6 on 2024-07-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='register',
            name='user_id',
        ),
        migrations.AddField(
            model_name='register',
            name='email_id',
            field=models.EmailField(default='example@example.com', max_length=50, unique=True),
        ),
    ]
