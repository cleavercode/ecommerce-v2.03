# Generated by Django 3.1.6 on 2021-05-10 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0006_auto_20210510_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupon.notification'),
        ),
    ]