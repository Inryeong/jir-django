# Generated by Django 3.1.2 on 2020-10-26 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('dsuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=1000, verbose_name='이미지 주소')),
                ('contents', models.TextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('tags', models.ManyToManyField(to='tag.Tag', verbose_name='태그')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsuser.dsuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '포스트',
                'verbose_name_plural': '포스트',
                'db_table': 'ds_post',
            },
        ),
    ]
