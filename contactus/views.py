from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response,  get_object_or_404
from contactus.models import Work_with_us, Work_for_us,Address

def contactus (request):
	return render_to_response('contactus.html', {
		'addresss': Address.objects.all()
		})
