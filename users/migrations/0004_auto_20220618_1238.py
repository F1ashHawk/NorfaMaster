# Generated by Django 2.1.5 on 2022-06-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220618_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_company',
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
