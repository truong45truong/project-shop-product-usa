# Generated by Django 3.2 on 2023-07-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_heart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
