from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.Home, name='Home' ),
    path('about/',views.about, name= "about"),
    path('contact/', views.contact, name="Contact"),
    path('service/', views.service, name="Services"),
    path('register/', views.register, name = "REGISTER"),
   # path('base/', views.one, name= "one")

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
