# Generated by Django 2.2.3 on 2019-07-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edamam_service', '0003_auto_20190712_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='foods',
            field=models.ManyToManyField(related_name='recipes', to='edamam_service.Food'),
        ),
    ]
