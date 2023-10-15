# Generated by Django 4.2.5 on 2023-10-14 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
