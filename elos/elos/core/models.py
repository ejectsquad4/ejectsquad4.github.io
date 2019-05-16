from django.db import models

class inicio(models.Model):
    titulo = models.CharField('Titulo', default='Inicio', max_length=100)
    tit_inic = models.TextField('Titulo do Inicio', default= 'Titulo do Inicio')
    subtit_inic = models.TextField('Subtitulo do Inicio', default='subtitulo')
    txt_bt_inic = models.CharField('Texto do botão', default='texto do botao', max_length=100)
    img_inic = models.ImageField(upload_to='img/img_inicio', verbose_name='Imagem do Inicio')

    class Meta:
        verbose_name = 'Início'
        verbose_name_plural = 'Início'

    def __str__(self):
        return self.titulo
    
class quem_somos(models.Model):
    titulo = models.CharField('Titulo', default='Quem Somos', max_length=100)
    tit_quem_somos = models.TextField('Titulo da descrição do projeto', default='Descrição do projeto')
    desc_quem_somos = models.TextField('Quem Somos')
    img_quem_somos = models.ImageField(upload_to='img/img_quem_somos', verbose_name='Imagem de Quem Somos')

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem somos'

    def __str__(self):
        return self.titulo
    
class clientes(models.Model):
    titulo = models.CharField('Cliente', default='Cliente', max_length=100)
    logo_clientes = models.ImageField(upload_to='img/img_clientes', verbose_name='Logo do Cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.titulo


class portfolio(models.Model):
    titulo = models.CharField('Titulo do Portifólio', default='titulo', max_length=100)
    img_portfolio = models.ImageField(upload_to='img/img_portfolio', verbose_name='Imagem do Portifólio')
    desc_portfolio = models.TextField('Portfólio')

    class Meta:
        verbose_name = 'Portifólio'
        verbose_name_plural = 'Portifólios'

    def __str__(self):
        return self.titulo

class serviços(models.Model):
    titulo = models.CharField('Titulo do serviço', default='titulo', max_length=100)
    img_serviço = models.ImageField(upload_to='img/img_serviço', verbose_name='Imagem do Serviço')
    desc_serviço = models.TextField('Serviço')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.titulo
