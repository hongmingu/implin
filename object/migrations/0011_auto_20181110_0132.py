# Generated by Django 2.0.5 on 2018-11-09 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('object', '0010_auto_20181110_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='chargelog',
            old_name='amount',
            new_name='gross',
        ),
        migrations.RenameField(
            model_name='paylog',
            old_name='amount',
            new_name='gross',
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='uuid',
            field=models.CharField(default='dafcdc5f02b74609846bc858a2c7d224', max_length=34, unique=True),
        ),
        migrations.AddField(
            model_name='chargelog',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='object.Wallet'),
        ),
        migrations.AddField(
            model_name='paylog',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='object.Wallet'),
        ),
        migrations.RemoveField(
            model_name='chargelog',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='chargelog',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='chargelog',
            unique_together={('wallet', 'transaction_id')},
        ),
        migrations.RemoveField(
            model_name='paylog',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='paylog',
            unique_together={('wallet', 'post')},
        ),
    ]
