# Generated by Django 3.0.7 on 2023-09-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20230927_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dia',
            field=models.CharField(choices=[('Segunda-Feira', 'Segunda-Feira'), ('Terça-Feira', 'Terça-Feira'), ('Quarta-Feira', 'Quarta-Feira'), ('Quinta-Feira', 'Quinta-Feira'), ('Sexta-Feira', 'Sexta-Feira'), ('Sábado-Feira', 'Sábado-Feira')], max_length=15, verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='horario',
            field=models.CharField(choices=[('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00')], max_length=10, verbose_name='Horario'),
        ),
    ]
