# Generated by Django 3.0 on 2020-06-02 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='massage',
            name='emai',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
