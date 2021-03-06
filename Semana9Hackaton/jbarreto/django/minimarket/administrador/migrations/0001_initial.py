# Generated by Django 3.0.8 on 2020-07-27 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cajero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechareporte', models.DateTimeField(auto_now_add=True)),
                ('fechainicio', models.DateTimeField()),
                ('fechafin', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cabcomprobantepago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.Cab_comprobantepago')),
            ],
        ),
    ]
