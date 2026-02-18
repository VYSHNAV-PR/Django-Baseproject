from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Book
from .forms import BookForm
# def home(request):
#    data={
#       'name':'vyshnav',
#       'age':24,
#       'mark':100
#    }
#    return render(request,'home.html',data)
#using for loop
def home(request):
   data=['python','javascript','html','css','react']
   return render(request,'home.html',{'a':data})
def about(request):
   return render(request,'about.html')
def contact(request):
   return render(request,'contact.html')
def viewbook(request):
   a=Book.objects.all()
   return render(request,'viewbook.html',{'book':a})  
def addbook(request):
   book=BookForm(request.POST or None)
   if book.is_valid():
      book.save()
      return redirect('viewbook')
   return render(request,'addbook.html',{'abc':book})
# Create your views here.
