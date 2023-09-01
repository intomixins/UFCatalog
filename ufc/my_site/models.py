from django.db import models


class Fighter(models.Model):
    """ модель бойца """
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    record = models.CharField(max_length=50)
    is_retired = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_champ = models.BooleanField(default=True)
    is_currect_champ = models.BooleanField(default=False)
    style = models.ForeignKey('Styles', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


class Styles(models.Model):
    """ модель стиля бойца """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
