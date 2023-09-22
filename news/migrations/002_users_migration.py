from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("news", "001_categories_migration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=False)),
                ("email", models.EmailField(max_length=200, null=False)),
                ("password", models.CharField(max_length=200, null=False)),
                ("role", models.CharField(max_length=200, null=False)),
            ],
        ),
    ]