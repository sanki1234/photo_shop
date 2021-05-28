from django.db import models

# Create your models here.
class category(models.Model):
    name= models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name

class photo(models.Model):
    category=models.ForeignKey(category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField()

    def __str__(self):
        return self.description