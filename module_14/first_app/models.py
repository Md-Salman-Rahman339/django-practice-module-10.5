from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    # big_integer_field = models.BigIntegerField()
    # binary_field = models.BinaryField(default=b'\x00')
    date_time_field = models.DateTimeField()
  

    def __str__(self):
        return f"Roll:{self.roll}-{self.name}"
