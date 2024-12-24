# Generated by Django 5.1.4 on 2024-12-18 02:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dynamics', '0009_remove_message_request_remove_chatmessage_request_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='content',
            new_name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='message_type',
            field=models.CharField(choices=[('general', 'General Message'), ('request_chat', 'Request Chat Message')], default='general', max_length=20),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('message', 'Message'), ('request_accepted', 'Request Accepted')], default='message', max_length=50),
        ),
        migrations.CreateModel(
            name='AcceptedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('accepted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='en_proceso', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_requests', to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(blank=True, default=24, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dynamics.solicitud')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dynamics.acceptedrequest'),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_received_messages', to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='Dynamics.acceptedrequest')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
