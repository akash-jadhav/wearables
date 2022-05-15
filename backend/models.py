from django.db import models

# Create your models here.


class VitalData(models.Model):
    VITAL_TYPE = [
        ("ECG", "ecg"),
        ("BP", "bp"),
    ]

    user_id = models.CharField(max_length=200)
    type = models.CharField(
        max_length=20, choices=VITAL_TYPE, null=False, blank=False)
    data = models.JSONField()
