from django.urls import path,include
from django.urls import re_path
from . import views as d
#from . import views


urlpatterns = [
    re_path("",d.CompanyApiView.as_view())
]