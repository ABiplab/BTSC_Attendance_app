# Generated by Django 2.2.5 on 2019-12-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=12)),
                ('contact_no2', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('d_o_b', models.DateField(max_length=200)),
                ('joining_date', models.DateField(max_length=200)),
                ('p_code', models.CharField(max_length=6)),
                ('Image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('about', models.TextField(blank=True)),
            ],
        ),
    ]
