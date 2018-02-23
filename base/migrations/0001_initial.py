# Generated by Django 2.0.2 on 2018-02-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('started', models.DateField()),
                ('finished', models.DateField()),
                ('description', models.TextField()),
                ('major', models.TextField()),
            ],
            options={
                'ordering': ['-started'],
            },
        ),
    ]
