# Generated by Django 2.2.2 on 2019-09-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainerName', models.CharField(max_length=50)),
                ('trainingName', models.CharField(max_length=50)),
                ('startDate', models.CharField(max_length=50)),
            ],
        ),
    ]
