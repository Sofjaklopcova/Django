from django.db import models


class Hrac(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno hrace', help_text='Zadejte jméno hrace',
                             error_messages={'blank': 'Jméno hrace musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení hrace', help_text='Zadejte příjmení autora',
                                error_messages={'blank': 'Příjmení hrace musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    fotografie = models.ImageField(upload_to='hraci', verbose_name='Fotografie')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Hrac'
        verbose_name_plural = 'Hraci'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Trener(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno trener', help_text='Zadejte jméno trenera',
                             error_messages={'blank': 'Jméno trenera musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení trenera', help_text='Zadejte příjmení trenera',
                                error_messages={'blank': 'Příjmení trenera musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    fotografie = models.ImageField(upload_to='hraci', verbose_name='Fotografie')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Trener'
        verbose_name_plural = 'Treneri'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Soutez(models.Model):
    druh = models.CharField(max_length=100, verbose_name='Název soutěže', help_text='Zadejte název soutěže',
                            error_messages={'blank': 'Název soutěže je povinný údaj'})

    class Meta:
        ordering = ['druh']
        verbose_name = 'Soutez'
        verbose_name_plural = 'Soutez'

    def __str__(self):
        return f'{self.druh}'


class Tym(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Nazev tymu', help_text='Zadejte nazev tymu',
                             error_messages={'blank': 'Nazev tymu knihy musí být vyplněn'})
    hraci = models.ManyToManyField(Hrac)
    Treneri = models.ManyToManyField(Trener)
    Soutezi = models.ForeignKey('Soutez', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Soutez')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Tym'
        verbose_name_plural = 'Tymy'
