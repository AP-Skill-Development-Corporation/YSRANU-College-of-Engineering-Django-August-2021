from django.urls import path
from . import views

urlpatterns = [
	path("profile/",views.profile,name="profile"),
	path("data/",views.data,name="data"),
]