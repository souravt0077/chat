# Generated by Django 4.1.7 on 2023-03-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='rooms',
            name='password',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
