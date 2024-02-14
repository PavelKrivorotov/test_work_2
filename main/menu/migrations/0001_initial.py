# Generated by Django 5.0.2 on 2024-02-12 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('root', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MenuRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='menu.menuitem')),
            ],
        ),
    ]
