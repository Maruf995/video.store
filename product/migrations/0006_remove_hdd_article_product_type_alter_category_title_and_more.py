# Generated by Django 5.0.3 on 2024-05-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_register_hdd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hdd',
            name='article',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='', max_length=20, verbose_name='Тип'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='product',
            field=models.TextField(max_length=5000, verbose_name='Используемое оборудование'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Предложение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='accommodation',
            field=models.CharField(max_length=30, verbose_name='Размещение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(max_length=100, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='form_factor',
            field=models.CharField(max_length=20, verbose_name='Форм Фактор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='microphone',
            field=models.CharField(max_length=30, verbose_name='Микрофон'),
        ),
        migrations.AlterField(
            model_name='readysolutions',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='readysolutions',
            name='short_description',
            field=models.CharField(max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='readysolutions',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Предложение'),
        ),
        migrations.AlterField(
            model_name='register',
            name='article',
            field=models.CharField(max_length=100, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='register',
            name='description',
            field=models.CharField(max_length=5000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='register',
            name='max_resolution',
            field=models.CharField(max_length=50, verbose_name='Максимально разрешение'),
        ),
        migrations.AlterField(
            model_name='register',
            name='nutrition',
            field=models.CharField(max_length=50, verbose_name='Питание'),
        ),
    ]