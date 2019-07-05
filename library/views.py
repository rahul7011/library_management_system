from django.shortcuts import render
from .models import books,sidebooks

# Create your views here.
def index(request):
    book = books.objects.all()
    sidebook = sidebooks.objects.all()


    return render(request,'index.html',{'book':book,'sidebook':sidebook})