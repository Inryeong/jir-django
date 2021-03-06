# Generated by Django 3.1.2 on 2020-10-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dsuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=128, verbose_name='아이디')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('password', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'ds_user',
            },
        ),
    ]
