# Generated by Django 5.1.4 on 2024-12-16 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dynamics', '0005_acceptedrequest_accepted_by_acceptedrequest_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptedrequest',
            name='request',
            field=models.ForeignKey(blank=True, default=24, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dynamics.solicitud'),
        ),
    ]
