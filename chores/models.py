from django.db import models
from django.conf import settings


class Household(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="households_created",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Roommate(models.Model):
    name = models.CharField(max_length=100)
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, related_name="roommates"
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="roommate_profile",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} ({self.household.name})"


class Chore(models.Model):
    STATUS_OPEN = "open"
    STATUS_DONE = "done"
    STATUS_CHOICES = [
        (STATUS_OPEN, "Open"),
        (STATUS_DONE, "Done"),
    ]

    title = models.CharField(max_length=200)
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, related_name="chores"
    )
    assigned_to = models.ForeignKey(
        Roommate, on_delete=models.CASCADE, related_name="chores"
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_OPEN
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.assigned_to.name}"
