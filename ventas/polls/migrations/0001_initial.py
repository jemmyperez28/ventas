# Generated by Django 3.0.1 on 2019-12-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('forma_pago', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
    ]