# Generated by Django 5.1.2 on 2024-11-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_buyer_password_alter_buyer_balance_alter_buyer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='password',
        ),
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
