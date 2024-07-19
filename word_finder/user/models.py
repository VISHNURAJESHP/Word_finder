from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField
    password = models.CharField(max_length=50)
    CreatedAt = models.DateField(auto_now_add=True)
    ModifiedAt = models.DateField(auto_now_add=True)

    def set_password(self, raw_password):
        self.set_password = make_password(raw_password)
        self.save()
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)