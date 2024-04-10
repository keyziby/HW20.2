# Generated by Django 5.0.3 on 2024-03-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
