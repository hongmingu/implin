# Generated by Django 2.0.5 on 2018-11-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0008_auto_20181108_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='uuid',
            field=models.CharField(default='b68213bbb2cb45779ec4e670dc4202ad', max_length=34, unique=True),
        ),
    ]