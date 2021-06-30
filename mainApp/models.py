from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors['name'] = "Name should be atleast 5 characters long"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias should be atleast 2 characters long"
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors["email"] = "Your email must be valid"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0 :
            errors["duplicate"] = "Email input is already in use"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        
        return errors

class User(models.Model):
    name = models.CharField(max_length=55)
    alias = models.CharField(max_length=55)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
