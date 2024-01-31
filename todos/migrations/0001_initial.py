# Generated by Django 5.0.1 on 2024-01-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('progress', models.IntegerField()),
                ('created_at', models.DateField()),
                ('completed_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending'), ('IP', 'In Progress'), ('TP', 'Task Postponded'), ('D', 'Task Deleted'), ('F', 'Failed')], max_length=2)),
            ],
        ),
    ]
