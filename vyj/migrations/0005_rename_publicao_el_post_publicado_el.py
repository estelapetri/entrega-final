# Generated by Django 4.1.3 on 2023-01-01 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyj', '0004_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publicao_el',
            new_name='publicado_el',
        ),
    ]