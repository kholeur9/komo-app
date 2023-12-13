# Generated by Django 3.2.13 on 2023-12-12 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(blank=True, max_length=9, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForfaitClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forfait_client', models.IntegerField(default=0)),
                ('date_Achat', models.DateField(default=0)),
                ('numero_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='CreditClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
                ('date_credit', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('forfait_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.forfaitclient')),
            ],
        ),
    ]
