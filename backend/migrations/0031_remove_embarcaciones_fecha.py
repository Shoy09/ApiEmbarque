# Generated by Django 4.2.8 on 2024-07-24 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_alter_embarcaciones_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embarcaciones',
            name='fecha',
        ),
    ]
