from . import views
from django.urls import path


app_name = 'bank'

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.dataform, name='dataform'),
    path('show', views.show, name='show')
]
