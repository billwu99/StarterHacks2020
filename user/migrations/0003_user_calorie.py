# Generated by Django 2.2.5 on 2020-01-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200118_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='calorie',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
