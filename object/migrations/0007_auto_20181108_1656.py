# Generated by Django 2.0.5 on 2018-11-08 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('object', '0006_auto_20181108_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='postchat',
            name='uuid',
            field=models.CharField(default='cf713ac8f6354b0c9bc5830bb6ad36fd', max_length=34, unique=True),
        ),
        migrations.AlterField(
            model_name='postchatrestmessage',
            name='uuid',
            field=models.CharField(default='673f02f521d44cd1921384d6c1c8042e', max_length=34, unique=True),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='uuid',
            field=models.CharField(default='553ebf2d71414d5b90edff739bd37b49', max_length=34, unique=True),
        ),
    ]
