from django.urls import path

from . import views

urlpatterns = [
    # ex: /lights/
    path('', views.index, name='index'),
    # ex: /lights/5/
    path('<int:light_id>/', views.detail, name='detail'),
    # ex: /lights/add/
    path('add/', views.add, name='add'),
    # ex: /lights/publish
    path('publish', views.publish_message, name='publish'),
]
