from django.urls import path

from . import views

urlpatterns = [
    # ex: /lights/
    path('', views.index, name='index'),
    # ex: /lights/5/
    path('<int:light_id>/', views.detail, name='detail'),
    # ex: /lights/add/
    path('add/', views.add, name='add'),
    # ex: /lights/5/delete/
    path('<int:light_id>/delete/', views.delete, name='delete'),
    # ex: /lights/5/publish/
    path('<int:light_id>/publish/', views.publish_message, name='publish'),
]
