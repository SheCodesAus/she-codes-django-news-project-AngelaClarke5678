# Generated by Django 4.0.1 on 2022-06-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='uncategorised', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('story_img', models.CharField(default='https://i.picsum.photos/id/1024/1920/1280.jpg', max_length=500)),
                ('category', models.CharField(default='uncategorised', max_length=255)),
            ],
        ),
    ]
