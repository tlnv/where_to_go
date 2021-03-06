# Generated by Django 3.2.3 on 2021-06-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('longtitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='where_to_go.place')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]
