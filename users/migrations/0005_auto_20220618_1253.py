# Generated by Django 2.1.5 on 2022-06-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220618_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_company',
            field=models.BooleanField(default=False),
        ),
    ]
