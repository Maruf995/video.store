# Generated by Django 5.0.1 on 2024-01-08 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_material_alter_category_title_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Материалы', 'verbose_name_plural': 'Материалы'},
        ),
    ]