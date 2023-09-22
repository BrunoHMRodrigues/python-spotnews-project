from django.db import migrations, models
from news.validators.validators import validate_title


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("news", "002_users_migration"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200, null=False, validators=[validate_title])),
                ("content", models.TextField(null=False)),
                ("author", models.ForeignKey('Users', on_delete=models.CASCADE)),
                ("created_at", models.DateField(null=False)),
                ("image", models.ImageField(upload_to='img/', blank=True, null=True)),
                ("categories", models.ManyToManyField('Categories', null=False)),
            ],
        ),
    ]