# Generated by Django 2.2 on 2020-10-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20201028_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]