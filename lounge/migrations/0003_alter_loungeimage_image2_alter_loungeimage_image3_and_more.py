# Generated by Django 5.0.6 on 2024-05-13 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_datahandling_policy_and_more'),
        ('lounge', '0002_alter_lounge_options_alter_loungeimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loungeimage',
            name='image2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_image', to='common.media', verbose_name='Second Image'),
        ),
        migrations.AlterField(
            model_name='loungeimage',
            name='image3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_image', to='common.media', verbose_name='Third Image'),
        ),
        migrations.AlterField(
            model_name='loungeimage',
            name='image4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fourth_image', to='common.media', verbose_name='Fourth Image'),
        ),
    ]
