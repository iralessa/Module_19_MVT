# Generated by Django 5.1.2 on 2024-11-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_remove_buyer_password_alter_buyer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
