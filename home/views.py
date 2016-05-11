from django.shortcuts import render, render_to_response,  get_object_or_404
from home.models import Testimonial , Key_Service,Hospitality ,Our_team, About ,Founder,Image, Brand, Our_Service

def home (request):
	return render_to_response('index.html', {
		'key_services': Key_Service.objects.all(),
		'hospitalities' : Hospitality.objects.all(),
		'testimonials': Testimonial.objects.all(),
		'images' : Image.objects.all()
		})

def about (request):
	return render_to_response('about-us.html', {
		'abouts': About.objects.all(),
		'founders' : Founder.objects.all(),
		'our_teams': Our_team.objects.all(),
		'images' : Image.objects.all()
		})

def brand (request):
	return render_to_response('brand.html', {
		'brands': Brand.objects.all(),
		'images' : Image.objects.all()
		})


def our_service (request):
	return render_to_response('our_services.html', {
		'our_services': Our_Service.objects.all(),
		'images' : Image.objects.all()
		})







# Create your views here.
