# Generated by Django 3.1 on 2020-08-15 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdds', '0003_auto_20200814_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('igv', models.BooleanField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
                ('tipoproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipoproductos')),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ubicacion', models.CharField(max_length=500)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipoclientes')),
                ('transportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.transportistas')),
            ],
        ),
        migrations.CreateModel(
            name='detallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.pedidos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.productos')),
            ],
        ),
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('docmento', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
                ('isActivo', models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2)),
                ('tipocliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipoclientes')),
                ('tipodocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdds.tipodocumentos')),
            ],
        ),
    ]
