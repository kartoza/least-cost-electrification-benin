# Generated by Django 2.2.12 on 2020-05-26 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0028_maplayer_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapSlugMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Map')),
            ],
        ),
    ]
