from django.db import models
from django.contrib.auth.models import User 
import random 
import string 
from django.utils.text import slugify

# Create your models here.

def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    slug = models.SlugField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task}"

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(generate_slug() + "-1!2@3#0)98*(7&^%$#$@" + self.user.username + '"-1!2@3#0)98*(7&^%$#$@"' + generate_slug())
        super(Todo, self).save(*args, **kwargs)

