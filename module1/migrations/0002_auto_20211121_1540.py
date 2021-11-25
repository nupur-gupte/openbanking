# Generated by Django 3.1.3 on 2021-11-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='bank',
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accno', models.IntegerField(default=0)),
                ('branch', models.CharField(max_length=20)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.bank')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='acc',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='module1.account'),
        ),
    ]
