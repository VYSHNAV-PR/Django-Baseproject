from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('viewbook/',views.viewbook,name='viewbook'),
    path('addbook/',views.addbook,name='addbook'),
    path('updatebook/<int:id>',views.updatebook,name='updatebook'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('register/',views.register,name='register')
    
]
