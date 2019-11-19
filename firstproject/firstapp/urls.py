from django.urls import path
from firstapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact us/',views.contact,name='contact'),
    path ('formpage/',views.form_view,name='form')
]