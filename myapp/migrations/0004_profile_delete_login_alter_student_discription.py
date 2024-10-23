# Generated by Django 5.0.6 on 2024-10-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_login_alter_student_age_alter_student_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('bio', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='student',
            name='discription',
            field=models.CharField(max_length=1000),
        ),
    ]
