from django.urls import path
from HospitalAPP import views

urlpatterns = [
    path('',views.home_view)

]

# import static files using dispaly all files store
from django.conf.urls.static import static
from django.conf import  settings


if settings.DEBUG:
    
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)