from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    def __str__(self) -> str:
        return f"{self.title} (publishing date: {self.published_date})"
