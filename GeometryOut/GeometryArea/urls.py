from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='homeG'),
    path('zip/', views.zipcode_view, name='zipArea')
]
