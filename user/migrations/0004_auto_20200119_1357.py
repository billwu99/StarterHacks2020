# Generated by Django 2.2.5 on 2020-01-19 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_calorie'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('first_name', 'last_name', 'email')},
        ),
    ]
