# Generated by Django 3.2 on 2023-03-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decryptRSA', '0005_auto_20230314_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceclient',
            name='date_activate',
            field=models.DateTimeField(null=True),
        ),
    ]