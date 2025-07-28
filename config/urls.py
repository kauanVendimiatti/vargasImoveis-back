from django.contrib import admin
from django.urls import path, include 
from core.views import AppView

urlpatterns = [
    path('admin/', admin.site.urls),
    # A função 'include' agora é reconhecida
    path('api/', include('core.urls')), 
    path('', AppView.as_view(), name='app'),
]