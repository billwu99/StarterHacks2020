# Generated by Django 2.2.5 on 2020-01-18 22:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('current_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desired_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('increment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
