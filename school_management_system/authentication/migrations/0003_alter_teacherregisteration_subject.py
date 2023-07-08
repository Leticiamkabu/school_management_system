# Generated by Django 4.2.2 on 2023-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_teacherregisteration_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherregisteration',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Science', 'Science'), ('Math', 'Math'), ('Music', 'Music'), ('Language', 'Language')], default='None', max_length=300),
        ),
    ]
