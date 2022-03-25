from django.urls import path
from.import views
urlpatterns = [

    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('contact/',views.Contact,name='contact'),
    path('contactme/',views.showcontact,name='contactme'),
    path('showdata/',views.show,name='showdata')
    
]