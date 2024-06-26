# Generated by Django 5.0.6 on 2024-05-16 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=45)),
                ('Description', models.TextField()),
                ('url_image', models.TextField()),
                ('Actors', models.ManyToManyField(related_name='movies', to='movie_actor_app.actor')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_actor_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movie_actor_app.movie')),
            ],
        ),
    ]
