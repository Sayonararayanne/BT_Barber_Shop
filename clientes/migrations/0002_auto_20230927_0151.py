# Generated by Django 3.0.7 on 2023-09-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='horario',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outros', 'Outros')], max_length=10, verbose_name='Horario'),
        ),
    ]
