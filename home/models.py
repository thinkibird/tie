# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.
class Image(models.Model):
	"""docstring for Image"""
	image_alt = models.CharField(max_length=30, blank= "False")
	image_title = models.CharField(max_length=30, blank= "False")
	image = models.ImageField(null ="True", blank= "True")
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering =["-timestamp", "-updated"]

	def __str__(self):
		return self.image_title

#End Image
    	
#Home 
class Key_Service(models.Model):
	title = models.CharField(max_length = 15 , null = "False", blank= "False")
	image = models.ForeignKey('Image',  blank="True", null= "True")
	description = RichTextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
  		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return (self.title)

class Hospitality(models.Model):
	title = models.CharField(max_length = 15 , null = "False", blank= "False")
	image = models.ForeignKey('Image', blank="True", null= "True")
	description = RichTextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
  		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return (self.title )


class Testimonial(models.Model):
	name= models.CharField(max_length=30, null="False")
	image= models.ForeignKey('Image',blank="True", null= "True")
	review =RichTextField()
	rating= models.IntegerField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return (self.name)

	class Meta:
		ordering = ["-timestamp", "-updated"]

#End Home






#Brands

class Brand(models.Model):
	brand = models.CharField(max_length = 15)
	overview = RichTextField()
	description = RichTextField()
	image = models.ForeignKey('Image', blank="True", null= "True")
	position = models.IntegerField(primary_key="True")
	website = models.URLField(blank= "True")
	fblink = models.URLField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	address = models.ForeignKey('contactus.Address')

	def __str__(self):
		return (self.brand )

	class Meta:
		ordering = ["-timestamp", "-updated"]

#end Brand




#About 
class About(models.Model):
	title = models.CharField(max_length = 15)
	overview = RichTextField()
	description = RichTextField()
	image = models.ForeignKey('Image', related_name= "About_Image")
	position = models.IntegerField( primary_key="True")


	def __str__(self):
		return (self.title )

	class Meta:
		ordering = ['position', ]

class Founder(models.Model):
	name = models.CharField(max_length =30, null ="False")
	designation = models.CharField(max_length=30 , null="False")
	founder_image= models.ForeignKey('Image')
	about = RichTextField()
	position = models.IntegerField( blank="False",  null="False")
	fblink= models.URLField(blank="False")
	twlink= models.URLField(blank="False")

	def __str__(self):
		return (self.name, self.designation)

	class Meta:
		ordering = ['position', ]

class Our_team(models.Model):
	name = models.CharField(max_length =30, null ="False")
	designation = models.CharField(max_length=30 , null="False")
	team_image= models.ForeignKey('Image')
	about = RichTextField()
	position = models.IntegerField( blank="False",  null="False")
	fblink= models.URLField(blank="False")
	twlink= models.URLField(blank="False")

	def __str__(self):
		return (self.name, self.designation)

	class Meta:
		ordering = ['position', ]
#End About 




# Our Services
class Our_Service(models.Model):
	title = models.CharField(max_length = 15)
	overview = RichTextField()
	description = RichTextField()
	image = models.ForeignKey('Image', blank= "True")
	position = models.IntegerField( primary_key="True")


	def __str__(self):
		return (self.title)

	class Meta:
		ordering = ['position', ]