from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f"{self.id} {self.username}"

    class Meta:
        db_table = "User"
