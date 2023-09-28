from django.forms import ModelForm
from .models import Cliente

class ClienteForm (ModelForm):

	class Meta:
		model = Cliente
		fields = ['nomecompleto', 'nascimento', 'sexo', 'horario', 'dia', 'whatsapp','endereco', 'cidade', 'email']
