# Generated by Django 3.1.6 on 2021-03-16 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Tipo: ')),
            ],
            options={
                'verbose_name': 'Tipo',
                'db_table': 'Tipo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.type'),
            preserve_default=False,
        ),
    ]
