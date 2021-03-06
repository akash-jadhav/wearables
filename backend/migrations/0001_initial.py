# Generated by Django 4.0.4 on 2022-05-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VitalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('ECG', 'ecg'), ('BP', 'bp')], max_length=20)),
                ('data', models.JSONField()),
            ],
        ),
    ]
