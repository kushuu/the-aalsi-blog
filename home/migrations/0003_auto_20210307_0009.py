# Generated by Django 3.1.3 on 2021-03-06 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210307_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='timestamp',
            new_name='date',
        ),
    ]