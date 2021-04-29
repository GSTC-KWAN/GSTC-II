# Generated by Django 2.2.7 on 2019-11-20 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20191120_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSN', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workingyears', models.CharField(max_length=200)),
                ('SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.SSN')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.SSN')),
            ],
        ),
        migrations.CreateModel(
            name='AnnualIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annualincome', models.CharField(max_length=200)),
                ('SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.SSN')),
            ],
        ),
    ]