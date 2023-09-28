from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outros', 'Outros')
    ]
    horario = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00')
    ]
    dia = [
        ('Segunda-Feira', 'Segunda-Feira'),
        ('Terça-Feira', 'Terça-Feira'),
        ('Quarta-Feira', 'Quarta-Feira'),
        ('Quinta-Feira', 'Quinta-Feira'),
        ('Sexta-Feira', 'Sexta-Feira'),
        ('Sábado-Feira', 'Sábado-Feira')

    ]
    
    nomecompleto = models.CharField('Nome Completo', max_length=150)
    nascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=9, choices=SEXO_CHOICES)
    horario = models.CharField('Horario', max_length=10, choices=horario)
    dia = models.CharField('Dia', max_length=15, choices=dia)
    whatsapp = models.CharField('Whatsapp', max_length=15)
    endereco = models.CharField('Endereço', max_length=150)
    cidade = models.CharField('Cidade', max_length=30)
    email = models.EmailField('Email')

    def __str__(self):
        return self.nomecompleto
