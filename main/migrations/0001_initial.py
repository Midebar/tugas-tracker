# Generated by Django 3.2.7 on 2024-02-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
