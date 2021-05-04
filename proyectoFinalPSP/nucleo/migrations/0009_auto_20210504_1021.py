# Generated by Django 3.2 on 2021-05-04 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nucleo', '0008_alter_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='idEmisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='idReceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensaje_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]