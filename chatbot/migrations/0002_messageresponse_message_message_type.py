# Generated by Django 4.2 on 2023-12-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField()),
                ('output_text', models.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='message_type',
            field=models.SmallIntegerField(choices=[('USER', 1), ('BOT', 1)], default=1),
        ),
    ]
