# Generated by Django 2.2.6 on 2019-10-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_condition_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='end_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='start_date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]