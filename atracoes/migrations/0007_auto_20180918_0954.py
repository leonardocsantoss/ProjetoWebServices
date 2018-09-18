# Generated by Django 2.1 on 2018-09-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0006_auto_20180912_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='bio',
            field=models.TextField(help_text='Uma breve descrição sobre a atração.', verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='atracao',
            name='site',
            field=models.URLField(help_text='https://instagram.com/', verbose_name='Site'),
        ),
    ]