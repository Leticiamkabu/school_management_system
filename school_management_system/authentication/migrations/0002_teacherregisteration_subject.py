# Generated by Django 4.2.2 on 2023-07-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherregisteration',
            name='subject',
            field=models.CharField(choices=[('English', 'English'), ('Science', 'Science'), ('Math', 'Math'), ('Music', 'Music'), ('Languages', 'Languages')], default='None', max_length=300),
        ),
    ]
