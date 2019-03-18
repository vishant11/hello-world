from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', hotel_image_view, name='image_upload'),
    path('success', success, name='success'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
    path('paginate', index, name = 'hotel_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
