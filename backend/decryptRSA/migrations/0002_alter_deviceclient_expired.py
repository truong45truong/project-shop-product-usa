# Generated by Django 3.2 on 2023-03-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decryptRSA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceclient',
            name='expired',
            field=models.IntegerField(),
        ),
    ]