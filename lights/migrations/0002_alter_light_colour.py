# Generated by Django 4.1.4 on 2023-10-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='colour',
            field=models.CharField(default='#989898', max_length=200),
        ),
    ]
