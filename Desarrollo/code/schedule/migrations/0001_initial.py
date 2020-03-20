# Generated by Django 3.0 on 2020-03-20 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name of course')),
                ('maxLength', models.IntegerField()),
                ('minLength', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_institutional', models.CharField(max_length=10, verbose_name='institutional code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_institutional', models.CharField(max_length=10, verbose_name='institutional code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Teacher')),
            ],
            options={
                'verbose_name_plural': 'Teacher Courses',
            },
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(to='schedule.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Student')),
            ],
            options={
                'verbose_name_plural': 'Student Courses',
            },
        ),
    ]
