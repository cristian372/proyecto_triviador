# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=200)),
                ('respuesta', models.CharField(max_length=200)),
                ('puntaje', models.IntegerField(null=True)),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tema', models.CharField(unique=True, max_length=150)),
                ('materia', models.CharField(max_length=150)),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='Tema',
            field=models.ForeignKey(to='trivia.Tema'),
            preserve_default=True,
        ),
    ]
