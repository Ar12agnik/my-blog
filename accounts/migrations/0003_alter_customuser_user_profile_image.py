# Generated by Django 5.0.7 on 2024-08-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_profile_image',
            field=models.ImageField(blank=True, default='profile_image/default.jpg', upload_to='profile_image'),
        ),
    ]
