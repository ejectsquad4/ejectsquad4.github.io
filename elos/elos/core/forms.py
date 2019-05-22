from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mails import send_mail_template

class Contato(forms.Form):
    nome = forms.CharField(error_messages={'required':'É importante para nós saber seu nome'}, widget=forms.TextInput(attrs={'type': 'text', 'placeholder':'NOME', 'name':'field1', 'class':'field-divided'}), label='Nome')
    telefone = forms.CharField(error_messages={'required':'É importante para nós saber seu telefone'}, widget=forms.TextInput(attrs={'type': 'text', 'placeholder':'TELEFONE', 'name':'field2', 'class':'field-divided'}), label='Telefone', max_length=50)
    email = forms.EmailField(error_messages={'required':'É importante para nós saber seu email'}, widget=forms.TextInput(attrs={'type': 'email', 'placeholder':'EMAIL', 'name':'field3', 'class':'field-long'}), label='E-mail')
    mensagem = forms.CharField(error_messages={'required':'Uma mensagem vazia não é uma mensagem de verdade'}, widget=forms.Textarea(attrs={'placeholder':'Mensagem', 'name':'field5', 'id':'field5', 'class':'field-long field-textarea'}), label='Mensagem', required=True)

    def send_mail(self):
        context = {
            'nome': self.cleaned_data['nome'],
            'telefone': self.cleaned_data['telefone'],
            'email': self.cleaned_data['email'],
            'mensagem': self.cleaned_data['mensagem'],
        }
        template_name = 'contato.html'
        send_mail_template(
            template_name, context, [settings.CONTACT_EMAIL]
        )
    