# Generated by Django 5.0.6 on 2024-08-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendoapp', '0005_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoinmueble',
            name='nombre',
            field=models.IntegerField(),
        ),
    ]