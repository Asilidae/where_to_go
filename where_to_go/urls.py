from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from places import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('tinymce/', include('tinymce.urls')),
                  path('', views.index),
                  path('places/<int:id>/', views.get_place_by_id, name='place'),
                  path('save-selected-places/', views.save_selected_places, name='save_selected_places'),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
