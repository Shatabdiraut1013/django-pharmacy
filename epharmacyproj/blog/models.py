from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default="")
    chead = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="media/images", default="")

    def __str__(self):
        return self.title

class Popularpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    poptitle = models.CharField(max_length=50)
    popauthor = models.CharField(max_length=50)
    pophead = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    popthumbnail = models.ImageField(upload_to="media/images", default="")

    def __str__(self):
        return self.poptitle