from django.urls import path

from . import views

app_name = 'psa'

urlpatterns = [
    path('nac/tools/', views.nac_tools, name='nac_tools'),
    path('nac/tools/license/', views.nac_license, name='nac_license'),
    path('nac/tools/update/', views.nac_update, name='nac_update'),
    path('userful-links/', views.useful_links, name='userful_links'),
]