

from django.contrib import admin
from django.urls import path
from myself.views import Myself

urlpatterns = [
    path('', Myself),
]
