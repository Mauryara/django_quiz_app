# Generated by Django 4.1.4 on 2023-01-09 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Category',
            new_name='category',
        ),
    ]
