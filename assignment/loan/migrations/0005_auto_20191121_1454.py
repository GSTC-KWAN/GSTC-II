# Generated by Django 2.2.7 on 2019-11-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20191121_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='annualincome_text',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name_text',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='platform',
            name='ssn_text',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='platform',
            name='workingyears_text',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
