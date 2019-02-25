from django.conf.urls import url
from core import views

urlpatterns = [
	url(r'^index', views.render_page),
	url(r'^points/', views.render_page_points)
]
