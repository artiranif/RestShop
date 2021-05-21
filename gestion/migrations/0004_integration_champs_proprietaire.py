# Generated by Django 3.1 on 2021-05-17 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0003_enseigne_nullable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commandes3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produits', models.ManyToManyField(to='gestion.Produits2')),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Propriétaire', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marque2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMarque', models.CharField(max_length=50)),
                ('proprietaires', models.ManyToManyField(related_name='Proprietaires', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Commandes1',
        ),
        migrations.AlterField(
            model_name='enseigne3',
            name='marqueEnseigne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque2'),
        ),
        migrations.AlterField(
            model_name='produits2',
            name='marqueProduits',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque2'),
        ),
        migrations.DeleteModel(
            name='Marque1',
        ),
    ]