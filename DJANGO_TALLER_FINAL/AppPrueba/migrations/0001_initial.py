# Generated by Django 4.1.1 on 2022-12-19 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('fechaInscripcion', models.DateField()),
                ('horainscripcion', models.TimeField()),
                ('estado', models.CharField(choices=[['Reservado', 'Reservado'], ['Completado', 'Completado'], ['Anulado', 'Anulado'], ['Sin asistencia', 'Sin asistencia']], max_length=50)),
                ('observacion', models.CharField(blank=True, max_length=50)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPrueba.institucion')),
            ],
        ),
    ]