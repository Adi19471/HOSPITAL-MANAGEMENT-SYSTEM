# Generated by Django 3.2.9 on 2021-11-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalAPP', '0002_auto_20211117_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]