# Generated by Django 3.1 on 2021-05-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0016_suppression_achat2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commandes6',
            old_name='produits',
            new_name='achats',
        ),
    ]
