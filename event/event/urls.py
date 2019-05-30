
from django.urls import path
from django.contrib import admin
from eventapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('candidate', views.candidate, name='candidate'),
    path('createevent', views.createevent, name='elements'),
    path('login', views.login1, name='login'),
    path('technical', views.technical, name='technical'),
    path('nontech', views.nontech, name='nontech'),
    path('cultural', views.cultural, name='cultural'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),

    path('signup', views.signup1, name='signup'),

    path('logout', views.logout1, name='logout'),

    path('venue', views.venue, name='venue')

]