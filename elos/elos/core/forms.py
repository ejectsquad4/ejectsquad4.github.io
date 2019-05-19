from django import forms

class Contato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50, initial='Nome')
    nome.widget.attrs.update(size='34')
    telefone = forms.CharField(label='Telefone', max_length=50, initial='Telefone')
    telefone.widget.attrs.update(size='34')
    email = forms.EmailField(label='E-mail', initial='E-mail')
    email.widget.attrs.update(size='73')
    mensagem = forms.CharField(
        label='Mensagem', widget=forms.Textarea, initial='Mensagem'
    )
    mensagem.widget.attrs.update(size='73')


    