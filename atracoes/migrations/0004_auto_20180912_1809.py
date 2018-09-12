# Generated by Django 2.1 on 2018-09-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_auto_20180912_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='bio',
            field=models.TextField(default='Uma breve descrição sobre a atração.', verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='atracao',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='atracao',
            name='site',
            field=models.URLField(default='ex: instagram.com/', verbose_name='Site'),
        ),
    ]