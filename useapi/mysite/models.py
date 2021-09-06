from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField(),
    title = models.CharField(max_length = 1000),
    content = models.CharField(max_length = 1000),
    writer = models.CharField(max_length = 1000),
    creat_at = models.DateTimeField(),
    update_at = models.DateTimeField(),