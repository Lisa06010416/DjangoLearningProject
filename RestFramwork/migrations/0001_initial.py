# Generated by Django 3.1.4 on 2020-12-25 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.TextField()),
                ('teacher_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.TextField()),
                ('student_id', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_student', to='RestFramwork.teacher')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
