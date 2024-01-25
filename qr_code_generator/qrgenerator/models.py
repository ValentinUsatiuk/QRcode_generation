from django.db import models


class QRCodeInfo(models.Model):
    data = models.TextField()
    color = models.CharField(max_length=20, default="black")
    size = models.PositiveIntegerField(default=20)
