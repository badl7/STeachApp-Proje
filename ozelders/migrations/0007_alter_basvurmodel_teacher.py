# Generated by Django 4.0.2 on 2022-02-24 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ozelders', '0006_alter_basvurmodel_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basvurmodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basvuru', to=settings.AUTH_USER_MODEL, verbose_name='Eğitmen'),
        ),
    ]