# Generated by Django 2.2.7 on 2019-11-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_platform_pred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='pred',
            field=models.CharField(max_length=200),
        ),
    ]
