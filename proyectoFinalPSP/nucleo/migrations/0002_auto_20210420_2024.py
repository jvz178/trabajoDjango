# Generated by Django 2.0.2 on 2021-04-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='WebUsuario',
        ),
    ]
