from django.core.exceptions import ValidationError


def validate_title(title):
    words = title.split()
    if len(words) < 2:
        raise ValidationError(("O título deve conter pelo menos 2 palavras."))
