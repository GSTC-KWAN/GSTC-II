# Generated by Django 2.2.7 on 2019-11-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_platform_predloan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='predloan',
            field=models.CharField(max_length=200),
        ),
    ]
