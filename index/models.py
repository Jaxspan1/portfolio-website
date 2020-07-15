from django.db import models


class AssistanceRequest(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
