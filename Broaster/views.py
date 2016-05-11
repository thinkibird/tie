# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def aboutus(request):
	return render(request, 'About-Us.html')


def menu(request):
	return render(request, 'Menu.html')


def gallery(request):
	return render(request, 'Gallery.html')


def contactus(request):
	return render(request, 'Conatct-Us.html')


def service(request):
	return render(request, 'Service.html')


