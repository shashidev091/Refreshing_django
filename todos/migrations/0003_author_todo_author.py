# Generated by Django 5.0.1 on 2024-02-01 19:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_completed_at_alter_todo_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=3)])),
                ('last_name', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=3)])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.author'),
        ),
    ]
