from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    #return render_to_response('index.html')
	return render(request, 'index.html')

def hello(request):
	return render(request, 'index.html') 

def test(request):
	return HttpResponse("sadkjklasjdkl;as;kdjlakjlds")

