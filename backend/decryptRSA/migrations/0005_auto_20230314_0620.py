# Generated by Django 3.2 on 2023-03-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decryptRSA', '0004_deviceclient_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceclient',
            name='private_key',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deviceclient',
            name='public_key',
            field=models.TextField(null=True),
        ),
    ]
