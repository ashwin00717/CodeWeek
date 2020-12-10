# Generated by Django 3.1.4 on 2020-12-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='INVTN_EMPL_PAY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPL_ID', models.CharField(max_length=4000)),
                ('SAL', models.IntegerField()),
                ('PAY_PERIOD', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='INVTN_OBJECT_KEY_LIST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBJECT_KEY', models.CharField(max_length=4000)),
                ('OBJECT_NAME', models.CharField(max_length=4000)),
                ('OBJECT_MASTER', models.CharField(max_length=4000)),
            ],
        ),
        migrations.RenameModel(
            old_name='IVNTN_OBJECT_KEY_LIST',
            new_name='INVTN_EMPL',
        ),
        migrations.RenameModel(
            old_name='IVNTN_IGNORE_KEY_LIST',
            new_name='INVTN_IGNORE_KEY_LIST',
        ),
        migrations.RenameModel(
            old_name='IVNTN_LOGIC_KEY_LIST',
            new_name='INVTN_LOGIC_KEY_LIST',
        ),
        migrations.RenameField(
            model_name='invtn_empl',
            old_name='OBJECT_MASTER',
            new_name='COUNTRY_CD',
        ),
        migrations.RenameField(
            model_name='invtn_empl',
            old_name='OBJECT_KEY',
            new_name='EMPL_ID',
        ),
        migrations.RenameField(
            model_name='invtn_empl',
            old_name='OBJECT_NAME',
            new_name='EMPL_NAME',
        ),
    ]