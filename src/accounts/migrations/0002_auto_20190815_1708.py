# Generated by Django 2.1 on 2019-08-15 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Cemail',
            new_name='confirm_email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Cpassword',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='lname',
            new_name='last_name',
        ),
    ]
