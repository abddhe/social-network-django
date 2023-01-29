from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self):
        return self.user.username


class Dweet(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.body
