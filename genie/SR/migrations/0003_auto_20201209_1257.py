# Generated by Django 3.1.4 on 2020-12-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR', '0002_auto_20201209_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='INVTN_EMPL',
        ),
        migrations.DeleteModel(
            name='INVTN_EMPL_PAY',
        ),
        migrations.DeleteModel(
            name='INVTN_IGNORE_KEY_LIST',
        ),
        migrations.DeleteModel(
            name='INVTN_LOGIC_KEY_LIST',
        ),
        migrations.DeleteModel(
            name='INVTN_OBJECT_KEY_LIST',
        ),
    ]
