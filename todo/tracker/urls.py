from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('impressum', views.impressum_view)
]
