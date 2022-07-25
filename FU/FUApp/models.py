from django.db import models

# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)
    profile_pic = models.ImageField('Profile Photo', upload_to='uploads/', null=True, blank=True)
    desc = models.TextField('User Description', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
