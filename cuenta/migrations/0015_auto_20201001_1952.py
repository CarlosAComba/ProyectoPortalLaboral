# Generated by Django 3.1.1 on 2020-10-01 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0014_auto_20201001_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='que_hacemos',
            old_name='para_que_te_sirve',
            new_name='porque_nosotros',
        ),
        migrations.RenameField(
            model_name='que_hacemos',
            old_name='que_hacemos',
            new_name='que_permite',
        ),
    ]
