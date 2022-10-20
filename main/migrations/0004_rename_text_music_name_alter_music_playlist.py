# Generated by Django 4.1.1 on 2022-10-20 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_musics_music'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='text',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='music',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='main.playlist'),
        ),
    ]
