# Generated by Django 4.0.5 on 2022-06-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='familiar',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
