# Generated by Django 4.2.7 on 2023-11-10 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_rename_langauges_langaugesmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SkillsModel',
            new_name='Langauges',
        ),
        migrations.RenameModel(
            old_name='LangaugesModel',
            new_name='Skills',
        ),
    ]
