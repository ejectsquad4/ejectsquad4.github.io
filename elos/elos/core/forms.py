from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mails import send_mail_template

class Contato(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder':'NOME', 'name':'field1', 'class':'field-divided'}), label='Nome')
    telefone = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder':'TELEFONE', 'name':'field2', 'class':'field-divided'}), label='Telefone', max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'placeholder':'EMAIL', 'name':'field3', 'class':'field-long'}), label='E-mail')
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensagem', 'name':'field5', 'id':'field5', 'class':'field-long field-textarea'}), label='Mensagem')

    def send_mail(self):
        mail_from = self.cleaned_data['email']
        context = {
            'nome': self.cleaned_data['nome'],
            'telefone': self.cleaned_data['telefone'],
            'email': self.cleaned_data['email'],
            'messagem': self.cleaned_data['messagem'],
        }
        template_name = 'templates/contato.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
    