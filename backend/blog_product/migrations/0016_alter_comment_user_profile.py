# Generated by Django 3.2 on 2023-04-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_product', '0015_alter_comment_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_profile',
            field=models.CharField(max_length=500, null=True),
        ),
    ]