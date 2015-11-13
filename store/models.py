from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail.shortcuts import get_thumbnail
#registration
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
   category = models.CharField(max_length=100)
   name = models.CharField(max_length=200)
   price = models.FloatField()
   brand = models.CharField(max_length=100, default="Verana")
  # image = models.ImageField(upload_to='static/bootstrap/itempics')
   is_active = models.BooleanField(default=True)
   details = models.CharField(max_length=250, default="-")
   times_clicked = models.IntegerField(default=0)
   is_recommended = models.BooleanField(default=False)
   is_popular = models.BooleanField(default=False)
   is_on_sale = models.BooleanField(default=False)
   is_new = models.BooleanField(default=False)
   volume = models.FloatField(default=0)
   weight= models.FloatField(default=0)
   code = models.CharField(max_length=50, default="000000")
   ingredients = models.CharField(max_length=200, default="-")
   tags = models.CharField(max_length=200, default="-")
   image = CloudinaryField(blank=True, null=True)


   def __str__(self):
		return self.name

   def get_thumbnail(self, size):
		img = self.image
		return unicode(get_thumbnail(img, '%(size)ix%(size)i' % {'size': size,}).url)

   def get_thumbnail_38(self):
		return self.get_thumbnail(38)

   def get_thumbnail_64(self):
		return self.get_thumbnail(64)

   def get_thumbnail_150(self):
		return self.get_thumbnail(150)

   def get_thumbnail_250(self):
		return self.get_thumbnail(250)

   def get_thumbnail_350(self):
		return self.get_thumbnail(350)

   def get_thumbnail_html(self):
		img_resize_url = self.get_thumbnail(100)
		html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
		return html % (self.image.url, img_resize_url, self.title)

#reg
class Address(models.Model):
	user=models.OneToOneField(User)
	country=models.CharField(max_length=50)
	postal_code=models.CharField(max_length=20)
	city=models.CharField(max_length=50)
	address=models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class Review(models.Model):
   product = models.ForeignKey(Product)
   user = models.ForeignKey(User, null=True)
   review_text = models.CharField(max_length=1000, default="")
   #author = models.CharField(max_length=30, default="Anonymous")
   is_shown = models.BooleanField(default=True)
   date_published = models.DateTimeField('date published')

   def __str__(self):
      return self.review_text