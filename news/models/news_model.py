from django.db import models
from news.validators.validators import validate_title


class News(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        validators=[validate_title],
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(null=False)
    image = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True,
    )
    categories = models.ManyToManyField(
        'Categories',
        null=False,
    )

    def __str__(self):
        return self.title
