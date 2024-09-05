# Generated by Django 5.0.6 on 2024-09-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterModelTable(
            name='onetimepassword',
            table='one_time_password',
        ),
    ]