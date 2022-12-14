# Generated by Django 4.0.4 on 2022-08-29 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_department_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=50)),
                ('house_no', models.CharField(max_length=50)),
                ('used', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_phone', models.CharField(max_length=3)),
                ('ccn_phone', models.CharField(max_length=15)),
                ('private_phone_1', models.CharField(max_length=15)),
                ('private_phone_2', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_relationship', models.CharField(choices=[('VO', 'V???'), ('CH', 'Ch???ng'), ('CO', 'Con'), ('BV', 'B??? V???'), ('MV', 'M??? V???'), ('BC', 'B??? Ch???ng'), ('MC', 'M??? Ch???ng')], max_length=2)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.phone')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.department')),
                ('peoplerelationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.peoplerelationship')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.phone')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.position')),
            ],
        ),
    ]
