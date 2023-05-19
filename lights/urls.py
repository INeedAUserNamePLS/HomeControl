from django.urls import path

from . import views

urlpatterns = [
    # ex: /lights/
    path('', views.index, name='index'),
    # ex: /lights/5/
    path('<int:light_id>/', views.detailLight, name='detailLight'),
    # ex: /lights/add/
    path('add/', views.addLight, name='addLight'),
    # ex: /lights/5/delete/
    path('<int:light_id>/delete/', views.deleteLight, name='deleteLight'),
    
    path('edit_broker', views.editBroker, name="editBroker"),
]
