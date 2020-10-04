# Generated by Django 3.0 on 2020-10-04 08:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Описание длинное'),
        ),
    ]