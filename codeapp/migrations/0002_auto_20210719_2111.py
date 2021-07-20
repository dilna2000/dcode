# Generated by Django 3.2.5 on 2021-07-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('points', models.IntegerField()),
                ('ques_attempted', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Points',
        ),
    ]