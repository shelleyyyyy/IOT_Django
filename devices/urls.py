from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URL configuation

urlpatterns = [
    path('hello/', views.hello_world),
    path('testJson/', views.profile),
    path('post_test/', views.post_test),
]
