# Generated by Django 2.1.7 on 2019-02-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("microsoft_auth", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="microsoftaccount",
            name="microsoft_id",
            field=models.CharField(
                max_length=36, verbose_name="microsoft account id"
            ),
        )
    ]
