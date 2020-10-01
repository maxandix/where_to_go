# Generated by Django 3.0 on 2020-09-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description_short', models.CharField(max_length=512, verbose_name='Описание короткое')),
                ('description_long', models.TextField(verbose_name='Описание длинное')),
                ('lat', models.FloatField(verbose_name='широта')),
                ('lon', models.FloatField(verbose_name='долгота')),
            ],
        ),
    ]
