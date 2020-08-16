from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    wname=models.CharField(max_length=70,default="")
    title=models.CharField(max_length=70, default="")
    head0=models.CharField(max_length=70, default="")
    chead0=models.CharField(max_length=7000, default="")
    head1=models.CharField(max_length=70, default="")
    chead1=models.CharField(max_length=7000, default="")
    head2=models.CharField(max_length=70, default="")
    chead2=models.CharField(max_length=7000, default="")
    pub_date = models.DateField()
    thumbnail=models.ImageField(upload_to='bloggerapp/images',default="")

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email =models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=15, default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name