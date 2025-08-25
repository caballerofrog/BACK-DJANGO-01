from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado'),
        ('descontinuado', 'Descontinuado'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    unidad = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre