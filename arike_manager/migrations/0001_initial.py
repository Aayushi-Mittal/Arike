# Generated by Django 4.0.2 on 2022-03-12 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('icds_code', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('kind', models.CharField(choices=[('PHC', 'PHC'), ('CHC', 'CHC')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lsg_body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('kind', models.IntegerField(choices=[(1, 'Grama Panchayath'), (2, 'Block Panchayath'), (3, 'District Panchayath'), (4, 'Nagar Panchayath'), (10, 'Municipality'), (20, 'Corporation'), (50, 'Others')])),
                ('lsg_body_code', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arike_manager.district')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('landmark', models.TextField()),
                ('phone', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100)),
                ('emergency_phone_number', models.CharField(max_length=30)),
                ('expired_time', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.facility')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule_Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=30)),
                ('lsg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arike_manager.lsg_body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visit_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('palliative_phase', models.CharField(max_length=255)),
                ('blood_pressure', models.CharField(max_length=255)),
                ('pulse', models.CharField(max_length=255)),
                ('general_random_blood_sugar', models.CharField(max_length=255)),
                ('personal_hygiene', models.CharField(max_length=255)),
                ('mouth_hygiene', models.CharField(max_length=255)),
                ('pubic_hygiene', models.CharField(max_length=255)),
                ('systemic_examination', models.CharField(max_length=255)),
                ('patient_at_peace', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=255)),
                ('pain', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=255)),
                ('symptoms', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
                ('visit_schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.schedule_visit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('role', models.CharField(choices=[('primary_nurse', 'primary_nurse'), ('secondary_nurse', 'secondary_nurse'), ('district_admin', 'district_admin')], max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('is_verified', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.district')),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.facility')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.TextField()),
                ('care_type', models.CharField(choices=[('General_care', 'General_care'), ('Genito_urinary_care', 'Genito_urinary_care')], max_length=255)),
                ('care_sub_type', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient_Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('note', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.disease')),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.patient')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.treatment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arike_manager.ward'),
        ),
        migrations.CreateModel(
            name='Family_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('relation', models.CharField(choices=[('MOTHER', 'MOTHER'), ('FATHER', 'FATHER'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('BROTHER', 'BROTHER'), ('SISTER', 'SISTER'), ('WIFE', 'WIFE'), ('HUSBAND', 'HUSBAND'), ('OTHER', 'OTHER')], max_length=100)),
                ('address', models.TextField()),
                ('education', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('remarks', models.TextField()),
                ('is_primary', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arike_manager.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='facility',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arike_manager.ward'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arike_manager.state'),
        ),
    ]