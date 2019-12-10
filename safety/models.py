from django.db import models
 
# Create your models here.
class Contact(models.Model):
	USER_TYPE_CHOICES = (
      (1, 'Normal_user'),
      (2, 'Lawyer'),)
    phone = models.IntegerField(max_length=11)
    name = models.CharField()
    email=models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     def __str__(self):
        return str(self.name)


 class Report(models.Model):
	REPORT_TYPE_CHOICES = (
	      (1, 'Robbery'),
	      (2, 'Harassmment'),)

 	date = models.DateField()
 	time =models.TimeField()
    location = models.CharField()
    report_type = models.PositiveSmallIntegerField(choices=REPORT_TYPE_CHOICES)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
        return str(self.report_type)

class Files(models.Model):
	FILE_TYPE_CHOICES = (
	      (1, 'Audio'),
	      (2, 'Video'),)
	path = models.IntegerField(max_length=11)
    sender = models.ForeignKey(User)
    to=models.CharField(unique=True)
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPE_CHOICES)
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)

     def __str__(self):
        return str(self.report_id)

