from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Sarlavha', max_length=60)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('Maqola')
    time = models.DateTimeField()

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title

