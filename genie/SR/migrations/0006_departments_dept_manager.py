# Generated by Django 3.1.4 on 2020-12-13 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SR', '0005_employee_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='dept_manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SR.departments')),
                ('emp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SR.employee')),
            ],
        ),
    ]
