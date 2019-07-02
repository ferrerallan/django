# Generated by Django 2.2.3 on 2019-07-02 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocalAtuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CentroCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('dtFim', models.DateField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Departamento')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Equipe')),
                ('gerencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Gerencia')),
                ('nucleo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Nucleo')),
            ],
        ),
    ]