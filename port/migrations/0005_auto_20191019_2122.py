# Generated by Django 2.2.6 on 2019-10-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_auto_20191019_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]