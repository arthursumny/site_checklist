from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    nome = models.CharField(max_length=100)
    link_venda = models.URLField()

    def __str__(self):
        return self.nome

class Checklist(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='checklists_images/')

    def __str__(self):
        return self.nome
