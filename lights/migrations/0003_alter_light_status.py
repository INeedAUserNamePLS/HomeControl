# Generated by Django 4.1.4 on 2023-10-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0002_alter_light_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
