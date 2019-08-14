from django.db import models

# Create your models here.
class Reg (models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dob = models.DateField()
    mob_no = models.IntegerField()
    email = models.EmailField(max_length=30)
    u_name = models.CharField(primary_key=True,max_length=30)
    p_word = models.CharField(max_length=20)
    cp_word = models.CharField(max_length=30)
    def __str__(self):
        return self.user