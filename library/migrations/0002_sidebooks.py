# Generated by Django 2.2.3 on 2019-07-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sidebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_author_name', models.CharField(max_length=100)),
                ('side_img', models.ImageField(upload_to='side')),
                ('side_book_title', models.CharField(max_length=100)),
            ],
        ),
    ]