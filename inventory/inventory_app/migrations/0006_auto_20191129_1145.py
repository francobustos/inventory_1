# Generated by Django 2.2.6 on 2019-11-29 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0005_auto_20191128_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trasladar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_traslado', models.DateTimeField()),
                ('area_de_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.Area')),
            ],
            options={
                'verbose_name': 'Trasladar',
                'verbose_name_plural': 'Traslado',
            },
        ),
        migrations.AlterField(
            model_name='objeto',
            name='fecha_entrada',
            field=models.DateField(blank=True, default='11/29/19', null=True),
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.AddField(
            model_name='trasladar',
            name='objeto',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory_app.Objeto'),
        ),
    ]