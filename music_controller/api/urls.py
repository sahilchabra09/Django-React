from django.urls import path
from .views import Roomview

urlpatterns = [
    path('' ,Roomview.as_view() )
]