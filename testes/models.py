from django.db import models

class Namelist(models.Model):
    name = models.CharField('Nome usuário', max_length=250)

    def __str__(self):
        return self.name


class Medidasteste(models.Model):
    nome = models.ForeignKey(Namelist, blank=True, null=True, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    estatura = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Ptronco = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Pcintura = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Pabdomen = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Pquadril = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PantebracoD = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PbracoD = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PcoxaD = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PpernaD = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Ir_vir = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Dinamometro = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Sentar_levantar = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Marcha = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.nome
