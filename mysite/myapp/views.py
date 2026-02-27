from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Book
from .forms import BookForm,UserRegisterForm,UserLoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
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
@login_required
def viewbook(request):
   a=Book.objects.all()
   return render(request,'viewbook.html',{'book':a})  
@login_required
def addbook(request):
   book=BookForm(request.POST or None,request.FILES or None)
   if book.is_valid():
      book.save()
      return redirect('viewbook')
   return render(request,'addbook.html',{'abc':book})
# Create your views here.
@login_required
def updatebook(request,id):
   book=Book.objects.get(id=id)
   form=BookForm(request.POST or None,request.FILES or None, instance=book)
   if form.is_valid():
      form.save()
      return redirect('viewbook')
   return render(request,'updatebook.html',{'abc':form})
@login_required
def deletebook(request,id):
   book=Book.objects.get(id=id)
   if request.method =='POST':
      book.delete()
      return redirect('viewbook')
def register(request):
   form=UserRegisterForm(request.POST or None)
   if request.method =='POST' and form.is_valid():
      form.save()
      return redirect('viewbook')
   return render(request,'register.html',{"form":form})
def login_form(request):
   forms=UserLoginForm(request,data=request.POST or None)
   if request.method == 'POST' and forms.is_valid():
      user=forms.get_user()
      login(request,user)
      return redirect('viewbook')
   return render(request,'login.html',{'form':forms})
def logout_form(request):
   logout(request)
   return redirect('login')