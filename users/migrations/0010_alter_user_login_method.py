# Generated by Django 3.2.7 on 2021-09-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_login_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('google', 'Google'), ('naver', 'Naver'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
