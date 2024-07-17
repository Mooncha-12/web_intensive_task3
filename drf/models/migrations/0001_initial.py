# Generated by Django 4.2.14 on 2024-07-17 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('years_of_experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cooking_time', models.DateField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='models.chef')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories_per_100g', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('dishes', models.ManyToManyField(related_name='ingredients', to='models.dish')),
            ],
        ),
    ]
