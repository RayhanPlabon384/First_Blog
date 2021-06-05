from django.db import models
from django.utils.html import format_html

# Create your models here.

#Category Model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name_plural="Category"
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px" />'.format(self.image))
    def __str__(self):
        return self.title
    
#Post Model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content =models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    
    class Meta:
        verbose_name_plural="Post"
        
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px" />'.format(self.image))
    def __str__(self):
        return self.title
    