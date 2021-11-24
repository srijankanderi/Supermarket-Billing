from django.conf.urls import url, include
from django.urls import path
from .views import ProductAPI

urlpatterns = [
	url(r'items/$', ProductAPI.as_view()),
]