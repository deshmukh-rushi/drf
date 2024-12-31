from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Name(View):
    n = '<h1> My name is Rushi</h1>'
    def get(self,request):
        return HttpResponse(self.n)