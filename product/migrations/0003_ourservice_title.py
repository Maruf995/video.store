# Generated by Django 4.2.11 on 2024-04-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_questions_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourservice',
            name='title',
            field=models.CharField(default='', max_length=400, verbose_name='название'),
            preserve_default=False,
        ),
    ]
