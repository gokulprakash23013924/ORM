# Generated by Django 5.0.2 on 2024-03-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOk',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('publisher_name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('publish_year', models.DateField()),
            ],
        ),
    ]
