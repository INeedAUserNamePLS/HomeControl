from django.urls import path

from . import views

urlpatterns = [
    # ex: /lights/
    path('', views.index, name='index'),
    # ex: /lights/5/
    path('<int:light_id>/', views.detailLight, name='detail'),
    # ex: /lights/add/
    path('add/', views.addLight, name='add'),
    # ex: /lights/5/delete/
    path('<int:light_id>/delete/', views.deleteLight, name='delete'),
     # ex: /lights/
    path('register', views.register, name='register'),
]
