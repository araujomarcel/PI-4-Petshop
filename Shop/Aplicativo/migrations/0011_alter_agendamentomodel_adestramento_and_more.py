# Generated by Django 5.0.4 on 2024-05-10 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicativo', '0010_agendamentomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentomodel',
            name='adestramento',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='atendimento24horas',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='atendimentodomiciliar',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='banhoetosa',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='consultaclinica',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='exameslaboratoriais',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='hospedagem',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='microchipagem',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='tosahigienica',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='transporte',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='vanicacao',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]