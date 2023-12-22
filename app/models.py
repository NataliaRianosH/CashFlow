from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255) 

    def __str__(self):
        return self.nombre_usuario

class ConceptoGasto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_concepto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_concepto

class Gasto(models.Model):
    id = models.AutoField(primary_key=True)
    concepto = models.ForeignKey(ConceptoGasto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    detalles = models.TextField(blank=True)
    emprendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Gasto de {self.emprendedor.nombre_usuario} - {self.fecha}"
