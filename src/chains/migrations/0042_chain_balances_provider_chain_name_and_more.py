# Generated by Django 4.2.2 on 2024-06-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chains", "0041_chain_prices_provider_chain_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="balances_provider_chain_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="chain",
            name="balances_provider_enabled",
            field=models.BooleanField(
                default=False,
                help_text="This flag informs API clients whether the balances provider is enabled for the chain",
            ),
        ),
    ]
