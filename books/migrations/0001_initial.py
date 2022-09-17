# Generated by Django 4.1.1 on 2022-09-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
