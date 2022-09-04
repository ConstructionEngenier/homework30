# Generated by Django 4.0.5 on 2022-07-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='member', max_length=9),
        ),
    ]
