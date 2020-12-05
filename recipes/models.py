from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=400)
    time = models.IntegerField()
    description = models.TextField()
    ingredients = models.CharField(max_length=1000)
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
