# Generated by Django 4.2.10 on 2024-07-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_createdat_alter_user_modifiedat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(),
        ),
    ]