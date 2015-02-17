# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import thuysses.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thuysse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annee', models.CharField(max_length=32, verbose_name=b'Ann\xc3\xa9e', choices=[(b'premiere', b'Premiere ann\xc3\xa9e'), (b'gm', b'Deuxieme ann\xc3\xa9e GM'), (b'gi', b'Deuxieme ann\xc3\xa9e GI'), (b'troisieme', b'Troisieme ann\xc3\xa9e')])),
                ('matiere', models.CharField(max_length=32, verbose_name=b'Mati\xc3\xa8re', choices=[(b'', b'-------'), (b'Anglais', b'Anglais'), (b'CEE', b'CEE'), (b'CM', b'CM'), (b'CPD', b'CPD'), (b'HSE', b'HSE'), (b'HSM', b'HSM'), (b'MAT', b'MAT'), (b'MDS', b'MDS'), (b'SIM', b'SIM'), (b'TDE', b'TDE'), (b'ESM', b'ESM'), (b'IND', b'IND'), (b'OPM', b'OPM'), (b'TCM', b'TCM'), (b'TDP', b'TDP'), (b'CM2', b'CM2'), (b'CMS', b'CMS'), (b'CSI', b'CSI'), (b'MSE', b'MSE'), (b'MSP', b'MSP'), (b'PJM', b'PJM')])),
                ('sous_matiere', models.CharField(blank=True, max_length=32, verbose_name=b'Sous mati\xc3\xa8re', choices=[(b'', b'----------------'), (b'M\xc3\xa9canique Vibratoire', b'M\xc3\xa9canique Vibratoire'), (b'M\xc3\xa9canique Non Lin\xc3\xa9aire', b'M\xc3\xa9canique Non Lin\xc3\xa9aire'), (b'M\xc3\xa9thodes Num\xc3\xa9riques', b'M\xc3\xa9thodes Num\xc3\xa9riques'), (b'Techniques Des Proc\xc3\xa9d\xc3\xa9s', b'Techniques Des Proc\xc3\xa9d\xc3\xa9s'), (b'Industrialisation', b'Industrialisation'), (b'Hydraulique', b'Hydraulique'), (b'Transfert M\xc3\xa9canique', b'Transfert M\xc3\xa9canique'), (b'Conversion Electrique', b'Conversion Electrique'), (b'Masse', b'Masse'), (b"Barral'ss", b"Barral'ss"), (b'Fabre', b'Fabre'), (b'Base de donn\xc3\xa9e-SQL', b'Base de donn\xc3\xa9e-SQL'), (b'Dufr\xc3\xa8ne', b'Dufr\xc3\xa8ne'), (b'Rosin-Bejaoui', b'Rosin-Bejaoui')])),
                ('genre', models.CharField(max_length=32, verbose_name=b'Genre', choices=[(b'Cours Amphi', b'Cours Amphi'), (b'ED', b'ED'), (b'TP', b'TP'), (b'Test', b'Test'), (b'Projet', b'Projet'), (b'Fiche', b'Fiche')])),
                ('date_DL', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nom de la thuysse')),
                ('auteur', models.CharField(max_length=32)),
                ('commentaire', models.TextField(blank=True)),
                ('fichier', models.FileField(upload_to=thuysses.models.get_path)),
                ('DL_Thuysse', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(to='users.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
