
from django.contrib import admin
from django.urls import path,include
from myself.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myself/', include('myself.urls')),
    path('', home),
]
