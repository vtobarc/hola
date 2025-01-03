# Generated by Django 5.1.4 on 2024-12-11 16:28

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cedula', models.CharField(default='0000000000', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Enter a valid cedula number.')])),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Enter a valid phone number.')])),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('Usuario', 'Usuario'), ('Servidor', 'Servidor')], max_length=50)),
                ('historial_tareas', models.TextField(blank=True, null=True)),
                ('preferencias', models.JSONField(blank=True, default=dict)),
                ('calificaciones', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil/')),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=10, null=True)),
                ('ultimo_acceso', models.DateTimeField(auto_now=True)),
                ('ip_registro', models.GenericIPAddressField(blank=True, null=True)),
                ('idioma_preferido', models.CharField(blank=True, choices=[('es', 'Español'), ('en', 'Inglés')], max_length=10, null=True)),
                ('titulo_profesional', models.CharField(blank=True, max_length=100, null=True)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('portfolio_url', models.URLField(blank=True, null=True)),
                ('habilidades_tecnicas', models.TextField(blank=True, null=True)),
                ('habilidades_blandas', models.TextField(blank=True, null=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='cover_photos/')),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='servicios/')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('precio_acordado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_limite', models.DateTimeField(blank=True, null=True)),
                ('progreso', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completado', 'Completado')], default='pendiente', max_length=50)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], default='pendiente', max_length=50)),
                ('valoraciones', models.IntegerField(blank=True, null=True)),
                ('metodo_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('archivos_adjuntos', models.FileField(blank=True, null=True, upload_to='archivos_adjuntos/')),
                ('tiempo_estimado', models.DurationField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('prioridad', models.CharField(max_length=100)),
                ('motivo_rechazo', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(choices=[('tecnologia', 'Tecnología'), ('diseno', 'Diseño'), ('marketing', 'Marketing'), ('escritura', 'Escritura y Traducción'), ('programacion', 'Programación y Desarrollo'), ('negocios', 'Negocios'), ('otros', 'Otros')], max_length=50)),
                ('precio_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo_estimado', models.DurationField(help_text='Tiempo estimado para completar el servicio')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='servicios/')),
                ('requisitos', models.TextField(blank=True, help_text='Requisitos para solicitar este servicio')),
                ('tags', models.CharField(blank=True, help_text='Tags separados por comas', max_length=255)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_ofrecidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tarjeta', models.CharField(max_length=50)),
                ('numero_tarjeta', models.CharField(max_length=16)),
                ('fecha_expiracion', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Dynamics.solicitud')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('descripcion', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
