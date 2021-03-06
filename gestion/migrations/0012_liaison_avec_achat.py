# Generated by Django 3.1 on 2021-05-20 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0011_creation_model_achat'),
    ]

    operations = [

        migrations.DeleteModel(
            name='Enseigne6',
        ),
        migrations.CreateModel(
            name='Achat2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Commandes6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Produits5',
            fields=[
                ('description', models.CharField(blank=True, max_length=200)),
                ('nomProduits', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('prix', models.FloatField()),
                ('marqueProduits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque4')),
            ],
        ),

        migrations.DeleteModel(
            name='Achat1',
        ),
        migrations.DeleteModel(
            name='Commandes5',
        ),
        migrations.AddField(
            model_name='commandes6',
            name='produits',
            field=models.ManyToManyField(through='gestion.Achat2', to='gestion.Produits5'),
        ),
        migrations.AddField(
            model_name='commandes6',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Propriétaire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='achat2',
            name='commande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.commandes6'),
        ),
        migrations.AddField(
            model_name='achat2',
            name='produitAchetee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.produits5'),
        ),
        migrations.DeleteModel(
            name='Produits4',
        ),
    ]
