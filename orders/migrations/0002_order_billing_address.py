# Generated by Django 3.2.4 on 2021-06-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]