# Generated by Django 3.2 on 2022-05-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loppis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='loppis',
            options={'verbose_name_plural': 'Loppises'},
        ),
    ]
