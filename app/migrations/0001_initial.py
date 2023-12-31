# Generated by Django 4.2.6 on 2023-10-31 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptoGasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_concepto', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
                ('detalles', models.TextField(blank=True)),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conceptogasto')),
                ('emprendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]
