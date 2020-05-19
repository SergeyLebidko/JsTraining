# Generated by Django 2.1.11 on 2020-05-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_order_dt_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Описание файла')),
                ('pdf_file', models.FileField(upload_to='', verbose_name='Прикрепленный файл')),
            ],
            options={
                'verbose_name': 'Документы',
            },
        ),
    ]
