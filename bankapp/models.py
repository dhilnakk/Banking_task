from django.db import models

# Create your models here.
class District(models.Model):
    dname=models.CharField(max_length=250)
    def __str__(self):
        return '{}'.format(self.dname)

class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE,related_name='branches')
    bname=models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.bname)