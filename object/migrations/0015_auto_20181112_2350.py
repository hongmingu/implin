# Generated by Django 2.0.5 on 2018-11-12 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0014_auto_20181112_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='SoloPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
                ('solo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo')),
            ],
        ),
        migrations.RemoveField(
            model_name='charge',
            name='user',
        ),
        migrations.RenameField(
            model_name='groupdatepay',
            old_name='amount',
            new_name='gross',
        ),
        migrations.RenameField(
            model_name='solodatepay',
            old_name='amount',
            new_name='gross',
        ),
        migrations.DeleteModel(
            name='Charge',
        ),
        migrations.AddField(
            model_name='solopost',
            name='solo_date_pay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SoloDatePay'),
        ),
        migrations.AddField(
            model_name='grouppost',
            name='group_date_pay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.GroupDatePay'),
        ),
        migrations.AddField(
            model_name='grouppost',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='solopost',
            unique_together={('solo', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='grouppost',
            unique_together={('group', 'post')},
        ),
    ]
