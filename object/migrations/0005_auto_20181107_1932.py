# Generated by Django 2.0.5 on 2018-11-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0004_auto_20181107_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDecimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decimal_10', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='postchat',
            name='uuid',
            field=models.CharField(default='7a74c35049a34e0d81acf5308958684c', max_length=34, unique=True),
        ),
        migrations.AlterField(
            model_name='postchatrestmessage',
            name='uuid',
            field=models.CharField(default='1b44a940d5854f27a6fd80b00b136226', max_length=34, unique=True),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='uuid',
            field=models.CharField(default='d4a48a41c0af42428b8c62b8433d9592', max_length=34, unique=True),
        ),
    ]
