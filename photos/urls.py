from django.urls import path
from . import views
urlpatterns=[
    path('',views.gallery,name="gallery"),
    path('add',views.add,name="add"),
    path('image/<str:pk>',views.image,name="image"),
]