from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_mainpage, name = 'index_mainpage'),
    url(r'^contacts/', views.contacts, name= 'contact'),
]