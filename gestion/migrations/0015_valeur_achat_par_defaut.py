# Generated by Django 3.1 on 2021-05-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0014_test_achat2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat2',
            name='nombre',
            field=models.PositiveIntegerField(default=1),
        ),
    ]