# Generated by Django 2.1.3 on 2018-12-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_authorizationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagestatus',
            name='message_status',
            field=models.CharField(choices=[('sending', 'sending'), ('canceled', 'canceled'), ('send', 'send'), ('sold', 'sold')], max_length=30),
        ),
    ]
