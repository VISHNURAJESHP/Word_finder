# Generated by Django 4.2.10 on 2024-07-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True, blank=True),
            preserve_default=False,
        ),
    ]
