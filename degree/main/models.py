from django.db import models
class Student(models.Model):
    secret_code=models.IntegerField(null=False)
    student_name=models.CharField(max_length=110,null=False)
    arabic_degree=models.FloatField(null=False)
    english_degree=models.FloatField(null=False)
    science_degree=models.FloatField(null=False)
    math_degree=models.FloatField(null=False)
    art_degree=models.FloatField(null=False)
    computer_degree=models.FloatField(null=False)
    french_degree=models.FloatField(null=False)
    english_level_degree=models.FloatField(null=False)
    region_degree=models.FloatField(null=False)
    def __str__(self):
        return self.student_name

# Create your models here.
