# Generated by Django 4.2.1 on 2023-05-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_account_active_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='secretToken',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]