# Generated by Django 3.1 on 2021-05-20 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_liaison_avec_achat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseigne7',
            fields=[
                ('adresse', models.CharField(max_length=75)),
                ('nomEnseigne', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('marqueEnseigne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque4')),
                ('produitPhare', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.produits5')),
            ],
        ),
    ]
