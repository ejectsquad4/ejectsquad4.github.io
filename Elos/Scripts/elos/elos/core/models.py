from django.db import models

class inicio(models.Model):
    titulo = models.CharField('Titulo do Inicio', default='titulo', max_length=100)
    img_inico = models.ImageField(upload_to='media/img/img_inicio', verbose_name='Imagem do Inicio')

    class Meta:
        verbose_name = 'Inicio'
        verbose_name_plural = 'Inicio'

    def __str__(self):
        return self.titulo
    
class quem_somos(models.Model):
    titulo = models.CharField('Titulo de Quem Somos', default='titulo', max_length=100)
    desc_quem_somos = models.TextField('Quem Somos')
    img_quem_somos = models.ImageField(upload_to='media/img/img_quem_somos', verbose_name='Imagem de Quem Somos')

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem somos'

    def __str__(self):
        return self.titulo
    
class clientes(models.Model):
    titulo = models.CharField('Titulo do Cliente', default='titulo', max_length=100)
    logo_clientes = models.ImageField(upload_to='media/img/img_clientes', verbose_name='Logo do Cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.titulo


class portfolio(models.Model):
    titulo = models.CharField('Titulo do Portifolio', default='titulo', max_length=100)
    img_portfolio = models.ImageField(upload_to='media/img/img_portfolio', verbose_name='Imagem do Portifolio')
    desc_portfolio = models.TextField('Quem Somos')

    class Meta:
        verbose_name = 'Portifólio'
        verbose_name_plural = 'Portifólios'

    def __str__(self):
        return self.titulo
