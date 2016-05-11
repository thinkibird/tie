# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Address(models.Model):
	name= models.CharField(max_length=30) 
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	phoneno = models.IntegerField()
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120, null=True, blank=True)
	zipcode = models.CharField(max_length=25)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	longitude = models.CharField(max_length=30, null=True)
	latitude = models.CharField(max_length=30, null=True)

	def __unicode__(self):
		return self.get_address()

	def get_address(self):
		return "%s, %s, %s, %s, %s" %(self.name, self.address, self.city, self.state, self.zipcode)  


class Work_with_us(models.Model):
	Name= models.CharField(max_length =30)
	Email = models.EmailField()
	PhoneNo = models.IntegerField()
	Address = models.CharField(max_length= 300)
	Details = models.TextField()


	def __unicode__(self):
		return self.withname()

	def withname(self):
		return "%s, %s, %s, %s" %(self.Name, self.PhoneNo, self.Email, self.Address)  


class Work_for_us(models.Model):
	Name= models.CharField(max_length =30)
	Email = models.EmailField()
	PhoneNo = models.IntegerField()
	Address = models.CharField(max_length= 300)
	Details = models.TextField()


	def __unicode__(self):
		return self.withname()

	def withname(self):
		return "%s, %s, %s, %s" %(self.Name, self.PhoneNo, self.Email, self.Address)  