# Generated by Django 4.2.7 on 2023-11-22 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numero', models.CharField(blank=True, max_length=45, primary_key=True, serialize=False)),
                ('cvv', models.CharField(blank=True, db_column='CVV', max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('fechaotorgamiento', models.DateField(blank=True, db_column='fechaOtorgamiento', null=True)),
                ('fechaexpiracion', models.DateField(blank=True, db_column='fechaExpiracion', null=True)),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
    ]
