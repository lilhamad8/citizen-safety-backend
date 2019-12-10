from django.db import models
from user.models import CustomUser
# Create your models here.
class Contact(models.Model):
        USER_TYPE_CHOICES = (
        (1, 'Normal_user'),
        (2, 'Lawyer'),)
        phone = models.IntegerField()
        name = models.CharField(max_length=50)
        email=models.EmailField(unique=True)
        user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        
        def __str__(self):
                return str(self.name)


class Report(models.Model):
        REPORT_TYPE_CHOICES = (
                (1, 'Robbery'),
                (2, 'Harassmment'),
                (3, 'Others'),)
        date = models.DateField()
        time =models.TimeField()
        location = models.CharField(max_length=200)
        report_type = models.PositiveSmallIntegerField(choices=REPORT_TYPE_CHOICES)
        sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        def __str__(self):
                return str(self.report_type)

class Files(models.Model):
        FILE_TYPE_CHOICES = (
                (1, 'Audio'),
                (2, 'Video'),)
        path = models.CharField(max_length=255)
        sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        to=models.CharField(max_length=255)
        file_type = models.PositiveSmallIntegerField(choices=FILE_TYPE_CHOICES)
        report_id = models.ForeignKey(Report, on_delete=models.CASCADE)

        def __str__(self):
                return str(self.report_id)

