# Generated by Django 2.2.3 on 2019-07-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile_no',
            field=models.CharField(max_length=20),
        ),
    ]
