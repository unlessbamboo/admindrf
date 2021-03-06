# coding:utf8
# Generated by Django 3.1.5 on 2021-01-31 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='书籍分类')),
                ('alias', models.CharField(max_length=32, verbose_name='分类别名')),
                ('description', models.CharField(max_length=128, verbose_name='别名介绍')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '书籍分类:社科,技术等',
                'db_table': 'booklabel',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=64, verbose_name='书籍名称')),
                ('publish', models.CharField(max_length=64, verbose_name='出版社')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('description', models.TextField(verbose_name='书籍描述信息')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('booklabel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.booklabel', verbose_name='书籍分类外键ID')),
            ],
            options={
                'verbose_name': '一个描述出版书籍的表信息',
                'db_table': 'book',
            },
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['name', 'author'], name='book_name_3d51f2_idx'),
        ),
    ]
