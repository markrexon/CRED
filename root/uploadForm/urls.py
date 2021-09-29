from django.urls import path
from .views import addData
urlpatterns=[
    path("",addData,name="allforms"),
]