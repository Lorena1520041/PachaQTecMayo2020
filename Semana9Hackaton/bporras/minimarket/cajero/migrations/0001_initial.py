# Generated by Django 3.0.8 on 2020-07-27 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almacen', '0001_initial'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fechaFact', models.DateTimeField(auto_now_add=True)),
                ('codAdministrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Administrador')),
                ('codCajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.Cajero')),
                ('codCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='FacturaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('codFacCabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.FacturaCabecera')),
                ('codProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.Producto')),
            ],
        ),
    ]