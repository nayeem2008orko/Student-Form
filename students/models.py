from django.db import models
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    subject = models.CharField(max_length=50)
    enrollment_year = models.CharField(max_length=20)
    highschool_cgpa = models.FloatField()
    eca_interest = models.CharField(max_length=10)
    eca_choice = models.CharField(max_length=50, blank=True, null=True)
    reason = models.TextField()

    def __str__(self):
        return self.full_name