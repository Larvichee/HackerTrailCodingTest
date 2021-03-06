# Generated by Django 3.1 on 2020-08-23 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_text', models.CharField(choices=[(0, '>_<'), (1, 'O_O'), (2, '>_>'), (3, ';_;')], default=0, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ProductArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_area_text', models.CharField(choices=[(0, 'Conquest'), (1, 'War'), (2, 'Famine'), (3, 'Plague')], default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descript', models.CharField(max_length=20000)),
                ('client_priority', models.IntegerField(default=0)),
                ('target_date', models.DateField()),
                ('client_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.client')),
                ('product_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.productarea')),
            ],
            options={
                'unique_together': {('client_type', 'client_priority')},
            },
        ),
    ]
