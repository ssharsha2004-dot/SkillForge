from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    skill = models.CharField(max_length=100)

    need = models.CharField(max_length=100)

    college = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class Resource(models.Model):

    title = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    description = models.TextField()

    link = models.URLField(
        blank=True,
        null=True
    )

    pdf = models.FileField(
        upload_to="resources/",
        blank=True,
        null=True
    )

    def __str__(self):

        return self.title