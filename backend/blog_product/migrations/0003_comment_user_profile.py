# Generated by Django 3.2 on 2023-04-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_product', '0002_auto_20230408_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.TextField(default='media/photos/user/images-12.jpeg'),
            preserve_default=False,
        ),
    ]