from django.forms import ModelForm
from CRUD.models import Pessoa

# Create the form class.
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'ultimo_nome', 'data_nascimento', 'profissao']