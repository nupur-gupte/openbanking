# Generated by Django 3.1.3 on 2021-11-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0008_user_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1234, max_length=10),
        ),
    ]
