# Generated by Django 4.2.2 on 2023-06-21 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_post_datecreation_post_rating_postcategory_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]