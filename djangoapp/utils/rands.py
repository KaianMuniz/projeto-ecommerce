import string
from random import SystemRandom
from django.utils.text import slugify

random = SystemRandom()


def random_letters(k=5):
    return ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=k)
    )


def slugify_new(text):
    return f'{slugify(text)}-{random_letters(5)}'