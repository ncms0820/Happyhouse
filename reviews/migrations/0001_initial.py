# Generated by Django 3.2.8 on 2021-10-31 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('review', models.TextField(max_length=255)),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('place', models.CharField(choices=[('guesthouse', 'guest house'), ('hairsalon', 'hairsalon'), ('facility', 'facility'), ('general', 'general')], default='general', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
