# Generated by Django 4.2.4 on 2023-09-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pchs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_name',
            name='com_password',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AddField(
            model_name='user_name',
            name='email',
            field=models.CharField(default='0', max_length=300),
        ),
        migrations.AddField(
            model_name='user_name',
            name='number',
            field=models.CharField(default='0', max_length=15),
        ),
        migrations.AddField(
            model_name='user_name',
            name='password',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AddField(
            model_name='user_name',
            name='user_name',
            field=models.CharField(default='0', max_length=200),
        ),
    ]