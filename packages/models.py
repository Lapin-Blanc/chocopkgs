from django.db import models


class ChocoPackage(models.Model):
    package_name = models.CharField('nom du paquet',
                                    max_length=50,
                                    unique=True)
    software_name = models.CharField('nom du logiciel',
                                     max_length=50,
                                     unique=True)
    software_description = models.CharField('description',
                                            max_length=200,
                                            blank=True,
                                            null=True)
    selected_by_default = models.BooleanField('sélectionné par défaut',
                                              default=True)

    def __str__(self):
        return f'{self.software_name} ({self.package_name})'

    class Meta:
        verbose_name = 'paquet'
        verbose_name_plural = 'paquets'
        ordering = ['package_name']
