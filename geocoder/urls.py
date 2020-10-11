from django.urls import path

from . import views

urlpatterns = [
    path('upload_excel_file/',  views.upload_excel_file,  name="upload_excel_file"),
    path('',  views.home,  name="home"),
]
