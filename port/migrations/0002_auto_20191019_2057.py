# Generated by Django 2.2.6 on 2019-10-19 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='select_code_text2',
            new_name='select_code_text3',
        ),
    ]
